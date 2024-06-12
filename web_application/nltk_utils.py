import numpy as np
import nltk
from nltk.stem.porter import PorterStemmer

class TextProcessor:
    def __init__(self):
        self.stemmer = PorterStemmer()

    def tokenize(self, sentence):
        return nltk.word_tokenize(sentence)

    def stem(self, word):
        return self.stemmer.stem(word.lower())

    def bag_of_words(self, tokenized_sentence, words):
        # Stem each word
        sentence_words = [self.stem(word) for word in tokenized_sentence]
        # Initialize bag with 0 for each word
        bag = np.zeros(len(words), dtype=np.float32)
        for idx, w in enumerate(words):
            if w in sentence_words:
                bag[idx] = 1
        return bag
