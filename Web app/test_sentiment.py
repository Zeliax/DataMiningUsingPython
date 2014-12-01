# coding=utf-8
from app.YouTubeConnection import youtube_search, comments_generator, get_video_name, get_video_link, get_video_rating, main_func
from app.sentimentAnalysis import wordlist_to_dict, sentiment, sentiment_analysis
from app.Plotter import pos_neg_counter, list_divider
from app.detect_lang import LanguageDetector
from gdata.youtube import service

WORDDICT = wordlist_to_dict()
TOKENIZED_WORDS = ['but', 'he', 'fails', 'miserably']
EMPTY_LIST = []
COMMENTSLIST = [['Lol I actually thought that was pretty good cause at first I'
                 ' thought it would just be legit cheesy haha']]
EMPTY_LIST_LIST = [[]]
ID_LIST = ['12g34h5T', 'sg09G876', '5A67sD89x']
ID = '-EBSfd3YlKQ'
URL = "https://www.youtube.com/watch?v=OoOHkJYeFDg"
YTS = service.YouTubeService()
POS_NEG_LIST = [3, 11, 9, 5, 6, 8]
POS_NEG_LISTS = [[1, 3, 6, 7], [0, 12, 3, 8, 9]]
LD = LanguageDetector()


def test_get_video_name():
    assert get_video_name(TOKENIZED_WORDS) == ['but', 'he', 'fails', 'miserably']


def test_get_video_link():
    assert get_video_link(ID_LIST) == ['https://www.youtube.com/watch?v=12g34h5T',
                                       'https://www.youtube.com/watch?v=sg09G876',
                                       'https://www.youtube.com/watch?v=5A67sD89x']


#def test_comments_generator():
#    assert comments_generator(YTS, ID) == '<generator object '
#    'comments_generator at 0x071A5918>'
# list(generator)


def test_pos_neg_counter():
    assert pos_neg_counter(POS_NEG_LIST) == [4, 2]


def test_list_divider():
    assert list_divider(POS_NEG_LISTS) == [[2, 2], [3, 2]]


#def test_main_func():
#    assert main_func(search_word, 1) == 


#def test_rating():
#    assert get_video_rating(URL) == [4579, 509]  # The rating changes with more likes/disklikes


def test_sentiment_value():
    assert sentiment(TOKENIZED_WORDS, WORDDICT) == [[4]]
    assert sentiment(EMPTY_LIST, WORDDICT) == [[]]
    assert sentiment(['is'], WORDDICT) == [[]]


def test_sentiment_analysis():
    assert sentiment_analysis(COMMENTSLIST, WORDDICT) == [[8.5]]
    assert sentiment_analysis(EMPTY_LIST_LIST, WORDDICT) == [[]]


def test_worddict():
    assert type(wordlist_to_dict()) == dict
    assert WORDDICT['happy'] == 9


def test_language_detector():
    assert LD.get_language('This is a lovely test for trying to figure out '
                           'the language.') == 'english'
    assert LD.get_language('Dette er en skøn test for at forsøge at finde ud '
                           ' af hvilket sprog det er') == 'danish'
    assert LD.get_language('C\'est un excellent metode pour détecter quelle '
                           ' langue il est!') == 'french'

#py.test test_sentiment.py
