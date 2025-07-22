# -*- coding: utf-8 -*-

"""
NLP Sentiment Analysis Project
This script trains a GRU-based model for sentiment analysis.
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from collections import Counter
import re

# 1. Data Preparation and Vocabulary Creation
class Vocabulary:
    def __init__(self, texts, unk_token='<unk>', pad_token='<pad>'):
        self.unk_token = unk_token
        self.pad_token = pad_token
        self.word_counts = Counter(word for text in texts for word in self.tokenize(text))
        self.vocab = sorted(self.word_counts, key=self.word_counts.get, reverse=True)
        self.word_to_idx = {word: i+2 for i, word in enumerate(self.vocab)}
        self.word_to_idx[pad_token] = 0
        self.word_to_idx[unk_token] = 1
        self.idx_to_word = {i: word for word, i in self.word_to_idx.items()}

    def tokenize(self, text):
        return re.findall(r'\w+', text.lower())

    def text_to_sequence(self, text):
        return [self.word_to_idx.get(word, self.word_to_idx[self.unk_token]) for word in self.tokenize(text)]

    def __len__(self):
        return len(self.word_to_idx)

def collate_fn(batch, pad_value=0):
    """Pads sequences in a batch to the same length."""
    sequences, labels = zip(*batch)
    max_len = max(len(seq) for seq in sequences)
    padded_sequences = torch.full((len(sequences), max_len), pad_value, dtype=torch.long)
    for i, seq in enumerate(sequences):
        padded_sequences[i, :len(seq)] = torch.tensor(seq)
    return padded_sequences, torch.tensor(labels, dtype=torch.float32)

# 2. Define the GRU Model
class SentimentGRU(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, output_dim, n_layers, dropout):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim, padding_idx=0)
        self.gru = nn.GRU(embedding_dim, hidden_dim, n_layers, batch_first=True, dropout=dropout if n_layers > 1 else 0)
        self.fc = nn.Linear(hidden_dim, output_dim)
        self.dropout = nn.Dropout(dropout)

    def forward(self, text):
        embedded = self.dropout(self.embedding(text))
        output, hidden = self.gru(embedded)
        # Use the last hidden state as the sentence representation
        return self.fc(self.dropout(hidden[-1,:,:]))

def main():
    # A slightly more realistic dataset
    texts = ["i love this movie, it's so great", "this is the best film ever", "amazing acting and plot",
             "i hate this, it's a terrible movie", "the worst film i have seen", "boring and long"]
    labels = [1, 1, 1, 0, 0, 0]

    vocab = Vocabulary(texts)
    sequences = [vocab.text_to_sequence(text) for text in texts]
    dataset = list(zip(sequences, labels))

    # Hyperparameters
    vocab_size = len(vocab)
    embedding_dim = 50
    hidden_dim = 128
    output_dim = 1
    n_layers = 2
    dropout = 0.5

    model = SentimentGRU(vocab_size, embedding_dim, hidden_dim, output_dim, n_layers, dropout)
    optimizer = optim.Adam(model.parameters())
    criterion = nn.BCEWithLogitsLoss() # More stable than BCELoss + Sigmoid

    dataloader = DataLoader(dataset, batch_size=2, shuffle=True, collate_fn=collate_fn)

    # Training
    model.train()
    for epoch in range(20):
        for seq, lab in dataloader:
            optimizer.zero_grad()
            output = model(seq).squeeze(1)
            loss = criterion(output, lab)
            loss.backward()
            optimizer.step()
        if (epoch+1) % 5 == 0:
            print(f'Epoch {epoch+1}, Loss: {loss.item():.4f}')

    # Inference
    model.eval()
    test_text = "the plot was fantastic and the acting was great"
    seq = torch.tensor(vocab.text_to_sequence(test_text)).unsqueeze(0)
    prediction = torch.sigmoid(model(seq))
    print(f'\nTest: "{test_text}" -> Prediction: {prediction.item():.2f} ({"Positive" if prediction.item() > 0.5 else "Negative"})')

if __name__ == '__main__':
    main()
