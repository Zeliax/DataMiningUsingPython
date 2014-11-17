from detect_lang import LanguageDetector
from nltk.tokenize import RegexpTokenizer
import numpy as np
import codecs


def wordlist_to_dict(list):
    """Creates a dictionary from a wordlist"""
    word_dict = {}
    s_line = []
    wordlist = codecs.open(list, "r", encoding='utf8')
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
    """Calculaltes the sentiment score from a tokenized sentence."""
    count = 0
    for word in words:
        if word in word_dict:
            count = count + int(word_dict[word])
            #print "The word is %s and the count is %d" %(word, count)
        else:
            #print "Word %s passed" %word
            pass
    # print "Total count is: %r" % count
    return count


def sentiment_analysis(commentlist, wordlist):
    """Calculates the sentiment of each comment and the total of all comments.

    Keyword arguments:
    commentlist -- a list of comments
    """
    #total_sentiment = 0
    tokenizer = RegexpTokenizer(r'[a-z]+')
    all_sentiments = []
    sent_sentiment = 100
    ld = LanguageDetector()
    for comment in commentlist:
        if ((ld.get_language(comment) == 'english') and (type(comment) is str)):
            comment = comment.lower()
            comment = " ".join([word for word in comment.split()
                                if "http" not in word])
            words = tokenizer.tokenize(comment)
            sent_sentiment = sentiment(words, wordlist)
            all_sentiments.append(sent_sentiment)
            mean_score = np.mean(all_sentiments)
            #total_sentiment += sent_sentiment
        else:
            pass
    return all_sentiments
