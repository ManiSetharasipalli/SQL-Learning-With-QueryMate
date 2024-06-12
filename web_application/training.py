import numpy as np
import random
import json
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from nltk_utils import TextProcessor
from chatbot_model import NeuralNet

class ChatBotTrainer:
    def __init__(self, intents):
        self.intents = intents
        self.text_processor = TextProcessor()
        self.all_words = []
        self.tags = []
        self.xy = []
        self.ignore_words = ['?', '.', '!', ',']
        self.X_train = None
        self.y_train = None
        self.num_epochs = 2000
        self.batch_size = 20
        self.learning_rate = 0.001
        self.input_size = None
        self.hidden_size = 10
        self.output_size = None
        self.dataset = None
        self.train_loader = None
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'

    def _preprocess_data(self):
        for intent in self.intents['intents']:
            tag = intent['tag']
            self.tags.append(tag)
            for pattern in intent['patterns']:
                w = self.text_processor.tokenize(pattern)
                self.all_words.extend(w)
                self.xy.append((w, tag))

        self.all_words = sorted(set([self.text_processor.stem(w) for w in self.all_words if w not in self.ignore_words]))
        self.tags = sorted(set(self.tags))

    def _create_training_data(self):
        self.X_train = []
        self.y_train = []
        for (pattern_sentence, tag) in self.xy:
            bag = self.text_processor.bag_of_words(pattern_sentence, self.all_words)
            self.X_train.append(bag)
            self.y_train.append(self.tags.index(tag))

        self.X_train = np.array(self.X_train)
        self.y_train = np.array(self.y_train)
        self.input_size = len(self.X_train[0])
        self.output_size = len(self.tags)

    def _create_dataloader(self):
        class ChatDataset(Dataset):
            def __init__(self, X, y):
                self.X = X
                self.y = y

            def __len__(self):
                return len(self.X)

            def __getitem__(self, idx):
                return self.X[idx], self.y[idx]

        self.dataset = ChatDataset(self.X_train, self.y_train)
        self.train_loader = DataLoader(self.dataset, batch_size=self.batch_size, shuffle=True)

    def train_model(self):
        model = NeuralNet(self.input_size, self.hidden_size, self.output_size).to(self.device)
        criterion = nn.CrossEntropyLoss()
        optimizer = torch.optim.Adam(model.parameters(), lr=self.learning_rate)

        for epoch in range(self.num_epochs):
            for batch_idx, (words, labels) in enumerate(self.train_loader):
                words = words.to(self.device)
                labels = labels.to(torch.long).to(self.device)

                optimizer.zero_grad()
                outputs = model(words)
                loss = criterion(outputs, labels)
                loss.backward()
                optimizer.step()

                if (batch_idx + 1) % 10 == 0:
                    print(
                        f'Epoch [{epoch + 1}/{self.num_epochs}], Batch [{batch_idx + 1}/{len(self.train_loader)}], Loss: {loss.item():.4f}')

        print(f'Final loss: {loss.item():.4f}')
        return model

    def save_model(self, model, file_path):
        data = {
            "model_state": model.state_dict(),
            "input_size": self.input_size,
            "hidden_size": self.hidden_size,
            "output_size": self.output_size,
            "all_words": self.all_words,
            "tags": self.tags
        }
        torch.save(data, file_path)
        print(f'Training complete. Model saved to {file_path}')

# Load intents data
with open('intents.json', 'r') as file:
    intents = json.load(file)

# Instantiate ChatBotTrainer
trainer = ChatBotTrainer(intents)

# Preprocess data
trainer._preprocess_data()

# Create training data
trainer._create_training_data()

# Create DataLoader
trainer._create_dataloader()

# Train the model
trained_model = trainer.train_model()

# Save the trained model
trainer.save_model(trained_model,"data.pth")
