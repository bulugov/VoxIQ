import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import numpy as np

# Define custom Siamese network
class SiameseNetwork(nn.Module):
    def __init__(self, input_size=13, hidden_size=128):
        super(SiameseNetwork, self).__init__()

        self.feature_extractor = nn.Sequential(
            nn.Linear(input_size, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, hidden_size),
            nn.ReLU(),
            nn.Flatten()
        )

        self.distance = nn.PairwiseDistance()

    def forward(self, input1, input2):
        output1 = self.feature_extractor(input1)
        output2 = self.feature_extractor(input2)
        return self.distance(output1, output2)

# Define custom contrastive loss function
class ContrastiveLoss(nn.Module):
    def __init__(self, margin=1.0):
        super(ContrastiveLoss, self).__init__()
        self.margin = margin

    def forward(self, output, target):
        euclidean_distance = output
        loss_contrastive = torch.mean((1 - target) * torch.pow(euclidean_distance, 2) +
                                      (target) * torch.pow(torch.clamp(self.margin - euclidean_distance, min=0.0), 2))
        return loss_contrastive

# Dummy dataset
class VoiceDataset(Dataset):
    def __init__(self, X1, X2, y):
        self.X1 = torch.FloatTensor(X1)
        self.X2 = torch.FloatTensor(X2)
        self.y = torch.FloatTensor(y)

    def __len__(self):
        return len(self.X1)

    def __getitem__(self, idx):
        return self.X1[idx], self.X2[idx], self.y[idx]

# Generate dummy data
X1 = np.random.rand(100, 13)
X2 = np.random.rand(100, 13)
y = np.random.randint(0, 2, size=(100,))

# Create datasets and dataloaders
dataset = VoiceDataset(X1, X2, y)
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

# Initialize the model, loss function, and optimizer
model = SiameseNetwork()
criterion = ContrastiveLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training loop
epochs = 10
for epoch in range(epochs):
    for input1, input2, labels in dataloader:
        optimizer.zero_grad()
        output = model(input1, input2)
        loss = criterion(output, labels)
        loss.backward()
        optimizer.step()

    print(f'Epoch {epoch+1}/{epochs}, Loss: {loss.item()}')
