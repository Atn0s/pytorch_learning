# -*- coding: utf-8 -*-

"""
NLP 情感分析项目
本脚本训练一个基于 GRU 的模型用于情感分析。
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from collections import Counter
import re

# 1. 数据准备和词汇表创建
class Vocabulary:
    """用于文本处理的词汇表类。"""
    def __init__(self, texts, unk_token='<unk>', pad_token='<pad>'):
        self.unk_token = unk_token
        self.pad_token = pad_token
        # 统计词频
        self.word_counts = Counter(word for text in texts for word in self.tokenize(text))
        # 按频率排序构建词汇表
        self.vocab = sorted(self.word_counts, key=self.word_counts.get, reverse=True)
        # 创建词到索引的映射
        self.word_to_idx = {word: i+2 for i, word in enumerate(self.vocab)}
        self.word_to_idx[pad_token] = 0
        self.word_to_idx[unk_token] = 1
        # 创建索引到词的映射
        self.idx_to_word = {i: word for word, i in self.word_to_idx.items()}

    def tokenize(self, text):
        """简单的分词器。"""
        return re.findall(r'\w+', text.lower())

    def text_to_sequence(self, text):
        """将文本转换为整数序列。"""
        return [self.word_to_idx.get(word, self.word_to_idx[self.unk_token]) for word in self.tokenize(text)]

    def __len__(self):
        return len(self.word_to_idx)

def collate_fn(batch, pad_value=0):
    """
    自定义的 collate_fn 函数，用于在 DataLoader 中对批次内的序列进行填充，
    使它们具有相同的长度。
    """
    sequences, labels = zip(*batch)
    max_len = max(len(seq) for seq in sequences)
    padded_sequences = torch.full((len(sequences), max_len), pad_value, dtype=torch.long)
    for i, seq in enumerate(sequences):
        padded_sequences[i, :len(seq)] = torch.tensor(seq)
    return padded_sequences, torch.tensor(labels, dtype=torch.float32)

# 2. 定义 GRU 模型
class SentimentGRU(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, output_dim, n_layers, dropout):
        super().__init__()
        # 词嵌入层
        self.embedding = nn.Embedding(vocab_size, embedding_dim, padding_idx=0)
        # GRU 层
        self.gru = nn.GRU(embedding_dim, hidden_dim, n_layers, batch_first=True, dropout=dropout if n_layers > 1 else 0)
        # 全连接层
        self.fc = nn.Linear(hidden_dim, output_dim)
        self.dropout = nn.Dropout(dropout)

    def forward(self, text):
        embedded = self.dropout(self.embedding(text))
        output, hidden = self.gru(embedded)
        # 使用最后一个隐藏状态作为句子的表示
        return self.fc(self.dropout(hidden[-1,:,:]))

def main():
    # 一个稍微更真实的数据集
    texts = ["i love this movie, it's so great", "this is the best film ever", "amazing acting and plot",
             "i hate this, it's a terrible movie", "the worst film i have seen", "boring and long"]
    labels = [1, 1, 1, 0, 0, 0]

    vocab = Vocabulary(texts)
    sequences = [vocab.text_to_sequence(text) for text in texts]
    dataset = list(zip(sequences, labels))

    # 超参数
    vocab_size = len(vocab)
    embedding_dim = 50
    hidden_dim = 128
    output_dim = 1
    n_layers = 2
    dropout = 0.5

    model = SentimentGRU(vocab_size, embedding_dim, hidden_dim, output_dim, n_layers, dropout)
    optimizer = optim.Adam(model.parameters())
    # BCEWithLogitsLoss 比 BCELoss + Sigmoid 更数值稳定
    criterion = nn.BCEWithLogitsLoss()

    dataloader = DataLoader(dataset, batch_size=2, shuffle=True, collate_fn=collate_fn)

    # 训练
    model.train()
    for epoch in range(20):
        for seq, lab in dataloader:
            optimizer.zero_grad()
            output = model(seq).squeeze(1)
            loss = criterion(output, lab)
            loss.backward()
            optimizer.step()
        if (epoch+1) % 5 == 0:
            print(f'周期 {epoch+1}, 损失: {loss.item():.4f}')

    # 推理
    model.eval()
    test_text = "the plot was fantastic and the acting was great"
    seq = torch.tensor(vocab.text_to_sequence(test_text)).unsqueeze(0)
    prediction = torch.sigmoid(model(seq)) # 使用 sigmoid 将输出转换为概率
    print(f'\n测试: "{test_text}" -> 预测: {prediction.item():.2f} ({"正面" if prediction.item() > 0.5 else "负面"})')

if __name__ == '__main__':
    main()
