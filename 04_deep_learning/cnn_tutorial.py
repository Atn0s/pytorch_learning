# -*- coding: utf-8 -*-

"""
PyTorch CNN Tutorial
This script demonstrates how to build, train, and evaluate a Convolutional Neural Network.
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# 1. Define a more modular CNN Architecture
class ConvBlock(nn.Module):
    """A single convolutional block."""
    def __init__(self, in_channels, out_channels, kernel_size=3, stride=1, padding=1):
        super(ConvBlock, self).__init__()
        self.conv = nn.Conv2d(in_channels, out_channels, kernel_size, stride, padding)
        self.bn = nn.BatchNorm2d(out_channels)
        self.relu = nn.ReLU()

    def forward(self, x):
        return self.relu(self.bn(self.conv(x)))

class AdvancedCNN(nn.Module):
    """A more advanced CNN for image classification."""
    def __init__(self, num_classes=10):
        super(AdvancedCNN, self).__init__()
        self.layer1 = ConvBlock(1, 32)
        self.layer2 = ConvBlock(32, 64)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.layer3 = ConvBlock(64, 128)
        self.layer4 = ConvBlock(128, 256)
        self.fc1 = nn.Linear(256 * 7 * 7, 512)
        self.dropout = nn.Dropout(0.5)
        self.fc2 = nn.Linear(512, num_classes)

    def forward(self, x):
        x = self.pool(self.layer2(self.layer1(x)))
        x = self.pool(self.layer4(self.layer3(x)))
        x = x.view(x.size(0), -1) # Flatten
        x = self.dropout(torch.relu(self.fc1(x)))
        x = self.fc2(x)
        return x

def main():
    """Main function to train and test the CNN."""
    print("--- PyTorch CNN Tutorial ---")

    # Hyperparameters & Device Config
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    batch_size = 128
    learning_rate = 0.001
    num_epochs = 5

    # 2. Data Augmentation and Loading
    print("\nApplying Data Augmentation...")
    train_transform = transforms.Compose([
        transforms.RandomRotation(10),
        transforms.RandomAffine(0, translate=(0.1, 0.1)),
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])
    test_transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])

    train_dataset = datasets.MNIST(root='./data', train=True, transform=train_transform, download=True)
    test_dataset = datasets.MNIST(root='./data', train=False, transform=test_transform)
    train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(dataset=test_dataset, batch_size=batch_size, shuffle=False)

    # 3. Model, Loss, Optimizer
    model = AdvancedCNN().to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)

    # 4. Training Loop
    print("\nStarting Training...")
    for epoch in range(num_epochs):
        model.train()
        for i, (images, labels) in enumerate(train_loader):
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            loss = criterion(outputs, labels)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            if (i+1) % 100 == 0:
                print(f'Epoch [{epoch+1}/{num_epochs}], Step [{i+1}/{len(train_loader)}], Loss: {loss.item():.4f}')

    # 5. Evaluation
    print("\nEvaluating model...")
    model.eval()
    with torch.no_grad():
        correct = 0
        total = 0
        for images, labels in test_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
        print(f'Test Accuracy: {100 * correct / total:.2f} %')

if __name__ == "__main__":
    main()
