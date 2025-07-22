# -*- coding: utf-8 -*-

"""
PyTorch CNN Tutorial
This script demonstrates how to build a Convolutional Neural Network (CNN) for image classification.
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms

# 1. Define the CNN Architecture
class SimpleCNN(nn.Module):
    """A simple CNN for image classification."""
    def __init__(self, num_classes=10):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=16, kernel_size=5, stride=1, padding=2)
        self.relu1 = nn.ReLU()
        self.pool1 = nn.MaxPool2d(kernel_size=2)

        self.conv2 = nn.Conv2d(in_channels=16, out_channels=32, kernel_size=5, stride=1, padding=2)
        self.relu2 = nn.ReLU()
        self.pool2 = nn.MaxPool2d(kernel_size=2)

        self.fc = nn.Linear(7*7*32, num_classes)

    def forward(self, x):
        out = self.pool1(self.relu1(self.conv1(x)))
        out = self.pool2(self.relu2(self.conv2(out)))
        out = out.view(-1, 7*7*32) # Flatten the tensor
        out = self.fc(out)
        return out

def main():
    """Main function to train and test the CNN."""
    print("--- PyTorch CNN Tutorial ---")

    # Hyperparameters
    batch_size = 64
    learning_rate = 0.001
    num_epochs = 3

    # 2. Load MNIST Dataset
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])

    train_dataset = datasets.MNIST(root='./data', train=True, transform=transform, download=True)
    test_dataset = datasets.MNIST(root='./data', train=False, transform=transform)

    train_loader = torch.utils.data.DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = torch.utils.data.DataLoader(dataset=test_dataset, batch_size=batch_size, shuffle=False)

    # 3. Instantiate the model, loss, and optimizer
    model = SimpleCNN()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)

    print("\nModel Architecture:")
    print(model)

    # 4. Training the CNN
    print("\nStarting Training...")
    for epoch in range(num_epochs):
        for i, (images, labels) in enumerate(train_loader):
            # Forward pass
            outputs = model(images)
            loss = criterion(outputs, labels)

            # Backward and optimize
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            if (i+1) % 200 == 0:
                print(f'Epoch [{epoch+1}/{num_epochs}], Step [{i+1}/{len(train_loader)}], Loss: {loss.item():.4f}')

    print("Training finished!")

    # 5. Testing the CNN
    print("\nTesting the model...")
    model.eval()
    with torch.no_grad():
        correct = 0
        total = 0
        for images, labels in test_loader:
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

        print(f'Accuracy of the model on the 10000 test images: {100 * correct / total} %')

if __name__ == "__main__":
    main()
