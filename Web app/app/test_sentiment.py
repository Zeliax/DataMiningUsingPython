#from detect_lang import LanguageDetector
from sentimentAnalysis import wordlist_to_dict, sentiment, sentiment_analysis

worddict = wordlist_to_dict("FINN-wordlist.txt")
tokenized_words = ['but', 'he', 'fails', 'miserably']


def test_sentiment_value():
    assert sentiment(tokenized_words, worddict) == -2




#py.test test_sentiment.py
