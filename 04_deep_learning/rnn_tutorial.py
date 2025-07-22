# -*- coding: utf-8 -*-

"""
PyTorch RNN/LSTM Tutorial
This script demonstrates how to build an LSTM for a sequence-to-one prediction task.
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader
import numpy as np

# 1. Define the LSTM Model
class AdvancedLSTM(nn.Module):
    """An LSTM model for sequence prediction."""
    def __init__(self, input_size, hidden_size, num_layers, output_size, dropout_prob=0.5):
        super(AdvancedLSTM, self).__init__()
        # Use LSTM which is better at capturing long-term dependencies
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True, bidirectional=True)
        self.dropout = nn.Dropout(dropout_prob)
        # We multiply hidden_size by 2 because of the bidirectional LSTM
        self.fc = nn.Linear(hidden_size * 2, output_size)

    def forward(self, x):
        # LSTM returns output and a tuple of hidden and cell states
        out, (h_n, c_n) = self.lstm(x)
        # We take the output from the last time step
        out = self.dropout(out[:, -1, :])
        out = self.fc(out)
        return out

def create_dataset(n_samples=1000, seq_length=20):
    """Creates a dummy dataset for a sine wave prediction task."""
    X = []
    y = []
    for _ in range(n_samples):
        start = np.random.rand() * 10
        time_steps = np.linspace(start, start + 5, seq_length + 1)
        sequence = np.sin(time_steps)
        X.append(sequence[:-1])
        y.append(sequence[-1])
    return torch.tensor(np.array(X), dtype=torch.float32).unsqueeze(-1), torch.tensor(np.array(y), dtype=torch.float32).unsqueeze(-1)

def main():
    """Main function to train and test the LSTM."""
    print("--- PyTorch LSTM Tutorial ---")

    # Hyperparameters
    input_size = 1
    hidden_size = 128
    num_layers = 2
    output_size = 1
    seq_length = 20
    learning_rate = 0.001
    num_epochs = 10
    batch_size = 64

    # 2. Create Dataset and DataLoader
    X_train, y_train = create_dataset(n_samples=5000, seq_length=seq_length)
    train_dataset = TensorDataset(X_train, y_train)
    train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)

    # 3. Model, Loss, Optimizer
    model = AdvancedLSTM(input_size, hidden_size, num_layers, output_size)
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)

    print("\nModel Architecture:")
    print(model)

    # 4. Training Loop
    print("\nStarting Training...")
    for epoch in range(num_epochs):
        model.train()
        for i, (sequences, labels) in enumerate(train_loader):
            outputs = model(sequences)
            loss = criterion(outputs, labels)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

    # 5. Inference
    print("\nMaking a prediction...")
    model.eval()
    with torch.no_grad():
        X_test, y_test = create_dataset(n_samples=1, seq_length=seq_length)
        prediction = model(X_test)
        print(f"Input sequence (last 5): {...X_test.squeeze().numpy()[-5:]}")
        print(f"Actual next value: {y_test.item():.4f}")
        print(f"Predicted next value: {prediction.item():.4f}")

if __name__ == "__main__":
    main()
