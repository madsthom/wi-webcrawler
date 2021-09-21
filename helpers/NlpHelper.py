import string

import nltk
from nltk import SnowballStemmer
from nltk.corpus import stopwords


def tokenize(string):
    return nltk.word_tokenize(string)


def stem(tokens):
    danish_stemmer = SnowballStemmer("danish")
    stemmed_tokens = []
    for t in tokens:
        stemmed_tokens.append(danish_stemmer.stem(t))
    return stemmed_tokens


def normalize(tokens):
    return [token.lower() for token in tokens]


def remove_stopwords(tokens: list[str]):
    stop_words = set(stopwords.words('english') + list(string.punctuation))
    return [token for token in tokens if token not in stop_words]
