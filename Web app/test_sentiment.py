# coding=utf-8

from app.sentimentAnalysis import wordlist_to_dict, sentiment, sentiment_analysis
from app.detect_lang import LanguageDetector

worddict = wordlist_to_dict()
tokenized_words = ['but', 'he', 'fails', 'miserably']
tokenized_empty = []
commentslist = [['Lol I actually thought that was pretty good cause at first I'
                 ' thought it would just be legit cheesy haha']]
commentlist = [[]]
ld = LanguageDetector()


def test_sentiment_value():
    assert sentiment(tokenized_words, worddict) == [-2]
    assert sentiment(tokenized_empty, worddict) == []
    assert sentiment('is', worddict) == []


def test_sentiment_analysis():
    assert sentiment_analysis(commentslist, worddict) == [2.5]
    assert sentiment_analysis(commentlist, worddict) == []


def test_worddict():
    assert type(wordlist_to_dict()) == dict
    assert worddict['happy'] == 3


def test_language_detector():
    assert ld.get_language('This is a lovely test for trying to figure out '
                           'the language.') == 'english'
    assert ld.get_language('Dette er en skøn test for at forsøge at finde ud '
                           ' af hvilket sprog det er') == 'danish'
    assert ld.get_language('C\'est un excellent metode pour détecter quelle '
                           ' langue il est!') == 'french'

#py.test test_sentiment.py
