from detect_lang import LanguageDetector
from nltk.tokenize import RegexpTokenizer
import numpy as np
import codecs
import os


def wordlist_to_dict():
    """Creates a dictionary from a wordlist"""
    path = os.getcwd()  # Runs from web app folder
    LIST = codecs.open(path + "\\app\\FINN-wordlist.txt", "r", encoding='utf8')
    word_dict = {}
    s_line = []
    for line in LIST:
        s_line.append(line.split('\t'))
    LIST.close()
    for word, sentiment in s_line:
        word_dict[word] = int(sentiment)
    return word_dict


def sentiment(words, word_dict):
    """Calculaltes the sentiment score for each word from a tokenized sentence'
       ' and stores them in a list."""
    sent_values = []
    for word in words:
        if word in word_dict:
            sent_values.append(word_dict[word])
            #print "The word is %s and the count is %d" %(word, count)
        else:
            #print "Word %s passed" %word
             sent_values.append(0)
    # print "Total count is: %r" % count
    return sent_values


def sentiment_analysis(commentlist, wordlist):
    """Calculates the mean sentiment of each comment.

    Keyword arguments:
    commentlist -- a list of lists of comments
    """
    #total_sentiment = 0
    tokenizer = RegexpTokenizer(r'[a-z]+')
    sent_sentiment = []
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
    return sent_sentiment
