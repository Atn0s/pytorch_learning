# -*- coding: utf-8 -*-

"""
NLP Sentiment Analysis Project
This script trains a simple LSTM model for sentiment analysis on a small, dummy dataset.
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

# 1. Prepare Data
def prepare_data():
    """Prepares a dummy dataset for sentiment analysis."""
    # Sample data: sentences and their sentiment (0: negative, 1: positive)
    texts = [
        "this movie is great", "i love this film", "what a fantastic movie",
        "this is a bad movie", "i hate this film", "what a terrible movie"
    ]
    labels = [1, 1, 1, 0, 0, 0]

    # Create a vocabulary
    word_to_idx = {}
    for text in texts:
        for word in text.split():
            if word not in word_to_idx:
                word_to_idx[word] = len(word_to_idx)

    # Convert texts to sequences of integers
    sequences = [[word_to_idx[word] for word in text.split()] for text in texts]

    # Pad sequences to the same length
    max_len = max(len(seq) for seq in sequences)
    padded_sequences = torch.zeros((len(sequences), max_len), dtype=torch.long)
    for i, seq in enumerate(sequences):
        padded_sequences[i, :len(seq)] = torch.tensor(seq)

    return padded_sequences, torch.tensor(labels, dtype=torch.float32), word_to_idx

# 2. Define the LSTM Model
class SentimentLSTM(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, output_dim):
        super(SentimentLSTM, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.lstm = nn.LSTM(embedding_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, output_dim)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        embedded = self.embedding(x)
        lstm_out, _ = self.lstm(embedded)
        # Take the output of the last time step
        final_output = lstm_out[:, -1, :]
        output = self.fc(final_output)
        return self.sigmoid(output)

def main():
    """Main function to train and test the sentiment analysis model."""
    print("--- NLP Sentiment Analysis Project ---")

    # Hyperparameters
    embedding_dim = 10
    hidden_dim = 16
    output_dim = 1
    learning_rate = 0.1
    num_epochs = 50

    # Prepare data
    sequences, labels, word_to_idx = prepare_data()
    vocab_size = len(word_to_idx)

    # Create DataLoader
    dataset = TensorDataset(sequences, labels)
    dataloader = DataLoader(dataset, batch_size=2)

    # Model, Loss, Optimizer
    model = SentimentLSTM(vocab_size, embedding_dim, hidden_dim, output_dim)
    criterion = nn.BCELoss() # Binary Cross-Entropy Loss
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)

    # Training Loop
    print("\nStarting Training...")
    for epoch in range(num_epochs):
        model.train()
        for batch_seq, batch_labels in dataloader:
            outputs = model(batch_seq).squeeze()
            loss = criterion(outputs, batch_labels)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        if (epoch+1) % 10 == 0:
            print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

    # Inference
    print("\nTesting the model...")
    model.eval()
    with torch.no_grad():
        for text in ["this film is fantastic", "this movie is bad"]:
            words = text.split()
            indexed = [word_to_idx.get(w, 0) for w in words]
            tensor = torch.LongTensor(indexed).unsqueeze(0)
            prediction = model(tensor)
            sentiment = "Positive" if prediction.item() > 0.5 else "Negative"
            print(f'Text: "{text}" -> Prediction: {prediction.item():.2f} ({sentiment})')

if __name__ == '__main__':
    main()
