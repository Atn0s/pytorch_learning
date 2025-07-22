# -*- coding: utf-8 -*-

"""
PyTorch CNN 教程
本脚本演示如何构建、训练和评估一个卷积神经网络。
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# 1. 定义一个模块化的 CNN 结构
class ConvBlock(nn.Module):
    """一个单独的卷积块，包含卷积、批归一化和激活函数。"""
    def __init__(self, in_channels, out_channels, kernel_size=3, stride=1, padding=1):
        super(ConvBlock, self).__init__()
        self.conv = nn.Conv2d(in_channels, out_channels, kernel_size, stride, padding)
        self.bn = nn.BatchNorm2d(out_channels)
        self.relu = nn.ReLU()

    def forward(self, x):
        return self.relu(self.bn(self.conv(x)))

class AdvancedCNN(nn.Module):
    """一个更高级的 CNN 模型，用于图像分类。"""
    def __init__(self, num_classes=10):
        super(AdvancedCNN, self).__init__()
        # 卷积层
        self.layer1 = ConvBlock(1, 32)
        self.layer2 = ConvBlock(32, 64)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2) # 池化层
        self.layer3 = ConvBlock(64, 128)
        self.layer4 = ConvBlock(128, 256)
        # 全连接层
        self.fc1 = nn.Linear(256 * 7 * 7, 512)
        self.dropout = nn.Dropout(0.5) # Dropout 层防止过拟合
        self.fc2 = nn.Linear(512, num_classes)

    def forward(self, x):
        x = self.pool(self.layer2(self.layer1(x)))
        x = self.pool(self.layer4(self.layer3(x)))
        x = x.view(x.size(0), -1) # 展平操作
        x = self.dropout(torch.relu(self.fc1(x)))
        x = self.fc2(x)
        return x

def main():
    """主函数，用于训练和测试 CNN。"""
    print("--- PyTorch CNN 教程 ---")

    # 超参数和设备配置
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    batch_size = 128
    learning_rate = 0.001
    num_epochs = 5

    # 2. 数据增强和加载
    print("\n应用数据增强...")
    # 训练集使用数据增强
    train_transform = transforms.Compose([
        transforms.RandomRotation(10), # 随机旋转
        transforms.RandomAffine(0, translate=(0.1, 0.1)), # 随机平移
        transforms.ToTensor(), # 转换为张量
        transforms.Normalize((0.1307,), (0.3081,)) # 标准化
    ])
    # 测试集不使用数据增强
    test_transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])

    train_dataset = datasets.MNIST(root='./data', train=True, transform=train_transform, download=True)
    test_dataset = datasets.MNIST(root='./data', train=False, transform=test_transform)
    train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(dataset=test_dataset, batch_size=batch_size, shuffle=False)

    # 3. 模型、损失函数和优化器
    model = AdvancedCNN().to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)

    # 4. 训练循环
    print("\n开始训练...")
    for epoch in range(num_epochs):
        model.train() # 设置为训练模式
        for i, (images, labels) in enumerate(train_loader):
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            loss = criterion(outputs, labels)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            if (i+1) % 100 == 0:
                print(f'周期 [{epoch+1}/{num_epochs}], 步骤 [{i+1}/{len(train_loader)}], 损失: {loss.item():.4f}')

    # 5. 评估
    print("\n评估模型...")
    model.eval() # 设置为评估模式
    with torch.no_grad():
        correct = 0
        total = 0
        for images, labels in test_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
        print(f'测试集准确率: {100 * correct / total:.2f} %')

if __name__ == "__main__":
    main()
