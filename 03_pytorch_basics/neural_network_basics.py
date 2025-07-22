# -*- coding: utf-8 -*-

"""
PyTorch Neural Network Basics
This script demonstrates how to build a simple neural network using torch.nn.
"""

import torch
import torch.nn as nn
import torch.optim as optim

# 1. Define the Neural Network
class SimpleNet(nn.Module):
    """A simple fully-connected neural network."""
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        """Forward pass through the network."""
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out

def main():
    """Main function to demonstrate neural network basics."""
    print("--- PyTorch Neural Network Basics ---")

    # Hyperparameters
    input_size = 10
    hidden_size = 32
    output_size = 1
    learning_rate = 0.01
    num_epochs = 5

    # 2. Instantiate the model, loss function, and optimizer
    model = SimpleNet(input_size, hidden_size, output_size)
    criterion = nn.MSELoss()  # Mean Squared Error for regression
    optimizer = optim.SGD(model.parameters(), lr=learning_rate)

    print("\nModel Architecture:")
    print(model)

    # 3. Generate some dummy data
    X_train = torch.randn(100, input_size)
    y_train = torch.randn(100, output_size)

    # 4. Training Loop
    print("\nStarting Training...")
    for epoch in range(num_epochs):
        # Forward pass
        outputs = model(X_train)
        loss = criterion(outputs, y_train)

        # Backward and optimize
        optimizer.zero_grad()  # Clear gradients from previous epoch
        loss.backward()
        optimizer.step()

        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

    print("Training finished!")

    # 5. Inference (making predictions)
    print("\nMaking a prediction...")
    # Create a new dummy input
    X_test = torch.randn(1, input_size)

    # Set the model to evaluation mode
    model.eval()

    with torch.no_grad():
        prediction = model(X_test)
        print(f"Input: {X_test}")
        print(f"Prediction: {prediction}")

if __name__ == "__main__":
    main()
