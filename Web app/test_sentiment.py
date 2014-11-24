# coding=utf-8

from app.sentimentAnalysis import wordlist_to_dict, sentiment, sentiment_analysis
from app.detect_lang import LanguageDetector

worddict = wordlist_to_dict()
tokenized_words = ['but', 'he', 'fails', 'miserably']


def test_sentiment_value():
    assert sentiment(tokenized_words, worddict) == -2

ld = LanguageDetector()


def test_language():
    assert ld.get_language('This is a lovely test for trying to figure out '
                           'the language.') == 'english'
    assert ld.get_language('Dette er en skøn test for at forsøge at finde ud '
                           ' af hvilket sprog det er') == 'danish'
    assert ld.get_language('C\'est un excellent metode pour détecter quelle '
                           ' langue il est!') == 'french'

#py.test test_sentiment.py
