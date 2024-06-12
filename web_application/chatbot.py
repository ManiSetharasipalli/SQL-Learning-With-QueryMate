import random
import json
import torch
from .chatbot_model import NeuralNet
from .nltk_utils import TextProcessor

class QueryMate:
    def __init__(self):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.bot_name = "QueryMate"
        self.model, self.all_words, self.tags, self.intents = self.load_model()
        self.text_processor=TextProcessor()

    def load_model(self):
        with open('web_application/intents.json', 'r') as json_data:
            intents = json.load(json_data)

        FILE = "web_application/data.pth"
        data = torch.load(FILE)

        input_size = data["input_size"]
        hidden_size = data["hidden_size"]
        output_size = data["output_size"]
        all_words = data['all_words']
        tags = data['tags']
        model_state = data["model_state"]

        model = NeuralNet(input_size, hidden_size, output_size).to(self.device)
        model.load_state_dict(model_state)
        model.eval()

        return model, all_words, tags, intents

    def get_response(self, msg):
        sentence = self.text_processor.tokenize(msg)
        X = self.text_processor.bag_of_words(sentence, self.all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X).to(self.device)

        output = self.model(X)
        _, predicted = torch.max(output, dim=1)

        tag = self.tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]
        if prob.item() > 0.90:
            for intent in self.intents['intents']:
                if tag == intent["tag"]:
                    return random.choice(intent['responses'])

        return "I'm sorry, I didn't quite catch that.If you have a SQL-related question, feel free to ask! For example, you could ask about specific SQL commands like 'show me an example of a WHERE clause' or 'explain JOIN operations.'"

# if __name__ == "__main__":
#     chatbot = QueryMate()
#     while True:
#         sentence = input()
#         if sentence == "quit":
#             break
#
#         resp = chatbot.get_response(sentence)
#         print(resp)
