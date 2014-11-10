from detect_lang import LanguageDetector
from nltk.tokenize import RegexpTokenizer
import numpy as np


def comments_to_list(textfile):
    """Creates a list of comments from a textfile"""
    commentlist = []
    comments = open(textfile, "r")
    for line in comments:
        commentlist.append(line)
    comments.close()
    return commentlist


def sentiment_analysis(commentlist, wordlist):
    """Calculates the sentiment of each comment and the total of all comments.

    Keyword arguments:
    commentlist -- a list of comments
    """
    #total_sentiment = 0
    tokenizer = RegexpTokenizer(r'[a-z]+')
    all_sentiments = []
    ld = LanguageDetector()
    for comment in commentlist:
        if ((ld.get_language(comment) == 'english') and (type(comment) is str)):
            comment = comment.lower()
            comment = " ".join([word for word in comment.split()
                                if "http" not in word])
            words = tokenizer.tokenize(comment)
            sent_sentiment = sentiment(words, wordlist)
            all_sentiments.append(sent_sentiment)
            #total_sentiment += sent_sentiment
        else:
            pass
    return np.mean(all_sentiments)


def sentiment(words, word_dict):
    """Calculaltes the sentiment score from a tokenized sentence."""
    count = 0
    for word in words:
        if word in word_dict:
            count = count + int(word_dict[word])
            #print "The word is %s and the count is %d" %(word, count)
        else:
            #print "Word %s passed" %word
            pass
    print "Total count is: %r" % count
    return count
