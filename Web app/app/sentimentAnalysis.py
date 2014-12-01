from detect_lang import LanguageDetector
from nltk.tokenize import RegexpTokenizer
import numpy as np
import codecs
import os


def wordlist_to_dict():
    """Creates a dictionary from a wordlist"""
    path = os.getcwd()  # Runs from web app folder
    word_list = codecs.open(path + "\\app\\FINN-wordlist.txt", "r", encoding='utf8')

    def parse_line(line):
        word, sentiment = line.split('\t')
        return word, int(sentiment)
    word_dict = dict([parse_line(line) for line in word_list])
    word_list.close()
    return word_dict


def sentiment(words, word_dict):
    """Calculaltes the sentiment score for each word from a tokenized sentence'
       ' and stores them in a list."""
    sent_values = []
    sent_values.append([word_dict[word] for word in words if word in word_dict])
    return sent_values


def sentiment_analysis(commentlist, wordlist):
    """Calculates the mean sentiment of each comment.

    Keyword arguments:
    commentlist -- a list of lists of comments
    """
    #total_sentiment = 0
    tokenizer = RegexpTokenizer(r'[a-z]+')
    sent_sentiment = []
    all_sentiment = []
    ld = LanguageDetector()
    for c_list in commentlist:
        for comment in c_list:
            if ((ld.get_language(comment) == 'english') and (type(comment) is str)):
                comment = comment.lower()
                comment = " ".join([word for word in comment.split()
                                    if "http" not in word])
                words = tokenizer.tokenize(comment)
                #sent_sentiment is a list of sentiments for each comment
                sent_sentiment.append(np.mean(sentiment(words, wordlist)))
        all_sentiment.append(sent_sentiment)
    return all_sentiment
