"""Contains the functions for making sentiment analysis."""
from detect_lang import LanguageDetector
from nltk.tokenize import RegexpTokenizer
import numpy as np
import codecs
import os


def wordlist_to_dict():
    """Create a dictionary from a wordlist."""
    path = os.getcwd()  # Runs from web app folder
    word_list = codecs.open(path + "\\app\\FINN-wordlist.txt", "r",
                            encoding='utf8')

    def parse_line(line):
        word, sentiment = line.split('\t')
        return word, int(sentiment)
    word_dict = dict([parse_line(line) for line in word_list])
    word_list.close()
    return word_dict


def sentiment(words, word_dict):
    """Calculalte the sentiment score.

    Calculates the sentiment score for each word from a tokenized sentence
    and stores them in a list.
    """
    sent_values = [word_dict[word] for word in words if word in word_dict]
    if not sent_values:
        sent_values = -1
    return sent_values


def sentiment_analysis(commentlist, wordlist):
    """Calculate the mean sentiment of each comment.

    Keyword arguments:
    commentlist -- a list of lists of comments
    """
    #total_sentiment = 0
    tokenizer = RegexpTokenizer(r'[a-z]+')
    all_sentiment = []
    neutral = []
    ld = LanguageDetector()
    for video in commentlist:
        video_sentiment = []
        for comment in video:
            if ((ld.get_language(comment) == 'english') and (type(comment) is
                                                             str)):
                comment = comment.lower()
                comment = " ".join([word for word in comment.split()
                                    if "http" not in word])
                words = tokenizer.tokenize(comment)
                sentiment_score = sentiment(words, wordlist)
                if sentiment_score == -1:
                    neutral.append(sentiment_score)
                else:
                # video_sentiment is a list of sentiments for each video.
                    video_sentiment.append(np.mean(sentiment_score))
        # all_sentiment is a list of sentiment scores for all the videos.
        all_sentiment.append(video_sentiment)
    return all_sentiment, neutral
