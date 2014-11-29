# coding=utf-8
from app.YouTubeConnection import youtube_search, split_video_list, comments_generator, get_video_name, get_video_link, get_video_rating, main_func
from app.sentimentAnalysis import wordlist_to_dict, sentiment, sentiment_analysis
from app.Plotter import pie_chart, hist_graph, pos_neg_counter, list_divider1, list_divider2
from app.detect_lang import LanguageDetector
from gdata.youtube import service
#from matplotlib.testing.decorators import cleanup

worddict = wordlist_to_dict()
tokenized_words = ['but', 'he', 'fails', 'miserably']
tokenized_empty = []
commentslist = [['Lol I actually thought that was pretty good cause at first I'
                 ' thought it would just be legit cheesy haha']]
commentlist = [[]]
IDlist = ['12g34h5T', 'sg09G876', '5A67sD89x']
ID = '-EBSfd3YlKQ'
url = "https://www.youtube.com/watch?v=OoOHkJYeFDg"
YTS = service.YouTubeService()
pos_neg_list = [3, 11, 9, 5, 6, 8]
list_ = [[1, 3, 6, 7], [0, 12, 3, 8, 9]]
ld = LanguageDetector()


def test_get_video_name():
    assert get_video_name(tokenized_words) == ['but', 'he', 'fails', 'miserably']


def test_get_video_link():
    assert get_video_link(IDlist) == ['https://www.youtube.com/watch?v=12g34h5T',
                                      'https://www.youtube.com/watch?v=sg09G876',
                                      'https://www.youtube.com/watch?v=5A67sD89x']


#def test_comments_generator():
#    assert comments_generator(YTS, ID) == '<generator object '
#    'comments_generator at 0x071A5918>'


def test_pos_neg_counter():
    assert pos_neg_counter(pos_neg_list) == [4, 2]


def test_list_divider():
    assert list_divider1(list_) == [[2, 2], [3, 2]]
    assert list_divider2(list_) == [[2, 2], [3, 2]]


#@cleanup
#def test_pie():
#    assert pie_chart([4, 2]) == figure()


#def test_main_func():
#    assert main_func(search_word, 1) == 


def test_rating():
    assert get_video_rating(url) == [4579, 509]


def test_sentiment_value():
    assert sentiment(tokenized_words, worddict) == [0, 0, 4, 0]
    assert sentiment(tokenized_empty, worddict) == []
    assert sentiment(['is'], worddict) == [0]


def test_sentiment_analysis():
    assert sentiment_analysis(commentslist, worddict) == [[1.7]]
    assert sentiment_analysis(commentlist, worddict) == [[]]


def test_worddict():
    assert type(wordlist_to_dict()) == dict
    assert worddict['happy'] == 9


def test_language_detector():
    assert ld.get_language('This is a lovely test for trying to figure out '
                           'the language.') == 'english'
    assert ld.get_language('Dette er en skøn test for at forsøge at finde ud '
                           ' af hvilket sprog det er') == 'danish'
    assert ld.get_language('C\'est un excellent metode pour détecter quelle '
                           ' langue il est!') == 'french'

#py.test test_sentiment.py
