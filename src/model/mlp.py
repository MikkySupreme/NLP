from nltk import DecisionTreeClassifier
from nltk.corpus import stopwords
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline

from src.features.text_features import stem_tokenizer


def make_model():
    return Pipeline([
        ("tfidf_vectorizer",
         TfidfVectorizer(tokenizer=stem_tokenizer, stop_words=stopwords.words('French'), strip_accents='unicode')),
        ("random_forest", MLPClassifier()),
    ])
