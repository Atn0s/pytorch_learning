# -*- coding: utf-8 -*-

"""
PyTorch Neural Network Basics
This script demonstrates how to build, train, and use a simple neural network.
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader

# 1. Define the Neural Network using nn.Sequential for simplicity
def create_model(input_size, hidden_size, output_size):
    """Creates a simple feed-forward network."""
    model = nn.Sequential(
        nn.Linear(input_size, hidden_size),
        nn.ReLU(),
        nn.Linear(hidden_size, hidden_size * 2),
        nn.ReLU(),
        nn.Linear(hidden_size * 2, output_size)
    )
    return model

def main():
    """Main function to demonstrate neural network basics."""
    print("--- PyTorch Neural Network Basics ---")

    # Hyperparameters
    input_size = 10
    hidden_size = 64
    output_size = 2 # Example for a 2-class classification
    learning_rate = 0.001
    num_epochs = 10
    batch_size = 32

    # 2. Create Model, Loss Function, and Optimizer
    model = create_model(input_size, hidden_size, output_size)
    criterion = nn.CrossEntropyLoss() # Suitable for classification
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)

    print("\nModel Architecture:")
    print(model)

    # 3. Data Loading
    # Generate dummy data
    X_train = torch.randn(500, input_size)
    y_train = torch.randint(0, output_size, (500,))
    # Create a dataset and dataloader
    train_dataset = TensorDataset(X_train, y_train)
    train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)

    # 4. Training Loop
    print("\nStarting Training...")
    for epoch in range(num_epochs):
        epoch_loss = 0.0
        for i, (inputs, labels) in enumerate(train_loader):
            # Forward pass
            outputs = model(inputs)
            loss = criterion(outputs, labels)

            # Backward and optimize
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            epoch_loss += loss.item()

        print(f'Epoch [{epoch+1}/{num_epochs}], Average Loss: {epoch_loss/len(train_loader):.4f}')
    print("Training finished!")

    # 5. Saving and Loading the Model
    print("\n5. Saving and Loading Model")
    # Save the model state dictionary
    torch.save(model.state_dict(), 'simple_net.pth')
    print("Model saved to simple_net.pth")

    # Load the model
    loaded_model = create_model(input_size, hidden_size, output_size)
    loaded_model.load_state_dict(torch.load('simple_net.pth'))
    loaded_model.eval() # Set to evaluation mode
    print("Model loaded from simple_net.pth")

    # 6. Inference
    print("\n6. Making a prediction")
    X_test = torch.randn(1, input_size)
    with torch.no_grad():
        prediction = loaded_model(X_test)
        predicted_class = torch.argmax(prediction, dim=1)
        print(f"Input: {X_test}")
        print(f"Output Raw: {prediction}")
        print(f"Predicted class: {predicted_class.item()}")

if __name__ == "__main__":
    main()
