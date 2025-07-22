# -*- coding: utf-8 -*-

"""
PyTorch 神经网络基础
本脚本演示如何构建、训练和使用一个简单的神经网络。
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader

# 1. 使用 nn.Sequential 定义一个简单的神经网络模型
def create_model(input_size, hidden_size, output_size):
    """创建一个简单的前馈网络。"""
    model = nn.Sequential(
        nn.Linear(input_size, hidden_size),
        nn.ReLU(),
        nn.Linear(hidden_size, hidden_size * 2),
        nn.ReLU(),
        nn.Linear(hidden_size * 2, output_size)
    )
    return model

def main():
    """主函数，用于演示神经网络的基础操作。"""
    print("--- PyTorch 神经网络基础 ---")

    # 超参数
    input_size = 10
    hidden_size = 64
    output_size = 2 # 假设是一个2分类问题
    learning_rate = 0.001
    num_epochs = 10
    batch_size = 32

    # 2. 创建模型、损失函数和优化器
    model = create_model(input_size, hidden_size, output_size)
    criterion = nn.CrossEntropyLoss() # 交叉熵损失，适用于分类问题
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)

    print("\n模型结构:")
    print(model)

    # 3. 数据加载
    # 生成一些虚拟数据
    X_train = torch.randn(500, input_size)
    y_train = torch.randint(0, output_size, (500,))
    # 创建一个数据集 (Dataset) 和数据加载器 (DataLoader)
    train_dataset = TensorDataset(X_train, y_train)
    train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)

    # 4. 训练循环
    print("\n开始训练...")
    for epoch in range(num_epochs):
        epoch_loss = 0.0
        for i, (inputs, labels) in enumerate(train_loader):
            # 前向传播
            outputs = model(inputs)
            loss = criterion(outputs, labels)

            # 反向传播和优化
            optimizer.zero_grad() # 清除上一轮的梯度
            loss.backward() # 计算当前梯度
            optimizer.step() # 更新权重

            epoch_loss += loss.item()

        print(f'周期 [{epoch+1}/{num_epochs}], 平均损失: {epoch_loss/len(train_loader):.4f}')
    print("训练完成!")

    # 5. 保存和加载模型
    print("\n5. 保存和加载模型")
    # 保存模型的状态字典
    torch.save(model.state_dict(), 'simple_net.pth')
    print("模型已保存至 simple_net.pth")

    # 加载模型
    loaded_model = create_model(input_size, hidden_size, output_size)
    loaded_model.load_state_dict(torch.load('simple_net.pth'))
    loaded_model.eval() # 切换到评估模式
    print("模型已从 simple_net.pth 加载")

    # 6. 推理 (Inference)
    print("\n6. 进行预测")
    X_test = torch.randn(1, input_size)
    with torch.no_grad(): # 推理时不需要计算梯度
        prediction = loaded_model(X_test)
        predicted_class = torch.argmax(prediction, dim=1)
        print(f"输入: {X_test}")
        print(f"原始输出: {prediction}")
        print(f"预测类别: {predicted_class.item()}")

if __name__ == "__main__":
    main()
