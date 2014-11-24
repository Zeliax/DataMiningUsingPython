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
    wordlist = LIST
    for line in wordlist:
        s_line.append(line.split('\t'))
    wordlist.close()
    for w, n in s_line:
        word_dict[w] = n
    return word_dict

#wordlist_to_dict("FINN-wordlist.txt")
#print word_dict['limited']


def comments_to_list(textfile):
    """Creates a list of comments from a textfile"""
    commentlist = []
    comments = open(textfile, "r")
    for line in comments:
        commentlist.append(line)
    comments.close()
    return commentlist


def sentiment(words, word_dict):
    """Calculaltes the sentiment score for each word from a tokenized sentence'
       ' and stores them in a list."""
    sent_values = []
    for word in words:
        if word in word_dict:
            sent_values.append(int(word_dict[word]))
            #print "The word is %s and the count is %d" %(word, count)
        else:
            #print "Word %s passed" %word
            pass
    # print "Total count is: %r" % count
    return sent_values


def sentiment_analysis(commentlist, wordlist):
    """Calculates the mean sentiment of each comment.

    Keyword arguments:
    commentlist -- a list of comments
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
            else:
                pass
    return sent_sentiment
