# -*- coding: utf-8 -*-

"""
PyTorch RNN Tutorial
This script demonstrates how to build a Recurrent Neural Network (RNN) for sequence modeling.
"""

import torch
import torch.nn as nn
import torch.optim as optim

# 1. Define the RNN Model
class SimpleRNN(nn.Module):
    """A simple RNN model."""
    def __init__(self, input_size, hidden_size, num_layers, output_size):
        super(SimpleRNN, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.rnn = nn.RNN(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        # Set initial hidden state
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size)

        # Forward propagate RNN
        out, _ = self.rnn(x, h0)

        # Decode the hidden state of the last time step
        out = self.fc(out[:, -1, :])
        return out

def main():
    """Main function to train and test the RNN."""
    print("--- PyTorch RNN Tutorial ---")

    # Hyperparameters
    input_size = 10
    hidden_size = 32
    num_layers = 2
    output_size = 1
    sequence_length = 5
    batch_size = 64
    learning_rate = 0.01
    num_epochs = 3

    # 2. Instantiate the model, loss, and optimizer
    model = SimpleRNN(input_size, hidden_size, num_layers, output_size)
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)

    print("\nModel Architecture:")
    print(model)

    # 3. Generate some dummy sequence data
    X_train = torch.randn(batch_size, sequence_length, input_size)
    y_train = torch.randn(batch_size, output_size)

    # 4. Training the RNN
    print("\nStarting Training...")
    for epoch in range(num_epochs):
        # Forward pass
        outputs = model(X_train)
        loss = criterion(outputs, y_train)

        # Backward and optimize
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

    print("Training finished!")

    # 5. Inference
    print("\nMaking a prediction on a new sequence...")
    model.eval()
    with torch.no_grad():
        X_test = torch.randn(1, sequence_length, input_size)
        prediction = model(X_test)
        print(f"Input sequence shape: {X_test.shape}")
        print(f"Prediction: {prediction}")

if __name__ == "__main__":
    main()
