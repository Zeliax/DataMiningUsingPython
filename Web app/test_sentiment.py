# coding=utf-8
""" Testing the functions in this final program."""
from app.YouTubeConnection import YouTubeConnection
from app.sentimentAnalysis import wordlist_to_dict, sentiment, sentiment_analysis
from app.Plotter import list_divider, generate_pie_plots, genereate_hist_plots
from app.detect_lang import LanguageDetector
from gdata.youtube import service
from app import config
import argparse
from app import app

WORDDICT = wordlist_to_dict()
SEARCH_WORD = 'cocio'
TOKENIZED_WORDS = ['but', 'he', 'fails', 'miserably']
EMPTY_LIST = []
COMMENTSLIST = [['Lol I actually thought that was pretty good cause at first I'
                 ' thought it would just be legit cheesy haha']]
EMPTY_LIST_LIST = [[]]
NO_WORDS = [['this is test']]
ID_LIST = ['12g34h5T', 'sg09G876', '5A67sD89x']
ID = '-EBSfd3YlKQ'
URL = ["https://www.youtube.com/watch?v=OoOHkJYeFDg"]
YTS = service.YouTubeService()
POS_NEG_LIST = [3, 11, 9, 5, 6, 8]
UNKNOWN_LIST = [-1, -1, -1, -1, -1]
POS_NEG_LISTS = [[1, 3, 6, 7], [0, 12, 3, 8, 9]]
LD = LanguageDetector()
developer_key = config.DEVELOPER_KEY
youtube_api_version = config.YOUTUBE_API_VERSION
youtube_api_service_name = config.YOUTUBE_API_SERVICE_NAME
YTC = YouTubeConnection(developer_key, youtube_api_version,
                        youtube_api_service_name)


def test_get_video_names():
    assert YTC.get_video_names(TOKENIZED_WORDS) == ['but', 'he', 'fails',
                                                    'miserably']


def test_get_video_links():
    link1 = 'https://www.youtube.com/watch?v=12g34h5T'
    link2 = 'https://www.youtube.com/watch?v=sg09G876'
    link3 = 'https://www.youtube.com/watch?v=5A67sD89x'
    assert YTC.get_video_links(ID_LIST) == [link1, link2, link3]


def test_get_embedded_links():
    link1 = 'https://www.youtube.com/embed/12g34h5T'
    link2 = 'https://www.youtube.com/embed/sg09G876'
    link3 = 'https://www.youtube.com/embed/5A67sD89x'
    assert YTC.get_embedded_links(ID_LIST) == [link1, link2, link3]


def test_comments_generator():
    assert len(list(YTC.comments_generator(ID))) >= -1


def test_yt_search():
    NR_OF_RESULTS = 1
    argparser = argparse.ArgumentParser(add_help=False)
    argparser.add_argument("--q", help="Search term", default=SEARCH_WORD)
    argparser.add_argument("--max-results", help="Max results",
                           default=NR_OF_RESULTS)
    args = argparser.parse_args()
    assert YTC.youtube_search(args) > 0
    NR_OF_RESULTS1 = 3
    SEARCH_WORD1 = '(2013-2014)'
    argparser1 = argparse.ArgumentParser(add_help=False)
    argparser1.add_argument("--q", help="Search term", default=SEARCH_WORD1)
    argparser1.add_argument("--max-results", help="Max results",
                            default=NR_OF_RESULTS1)
    args1 = argparser1.parse_args()
    assert YTC.youtube_search(args1) > 0  # Testing for parenthesis in name


def test_webapp():
    client = app.test_client()
    frontpage = client.get('/')
    assert frontpage._status == "200 OK"
    search_page = client.get('/search')
    assert search_page._status == "200 OK"


def test_main_func():
    assert YTC.main_func(SEARCH_WORD, 1) > 0


def test_rating():
    assert YTC.get_video_rating(URL) >= [4579, 509]


def test_generate_pie_plots():
    assert len(generate_pie_plots([[400, 100]], [[345, 59]], UNKNOWN_LIST)) > 0


def test_genereate_hist_plots():
    assert len(genereate_hist_plots(POS_NEG_LISTS, range(0, 13),
                                    [[-1, -1, -1], [-1, -1, -1]])) > 0




def test_list_divider():
    assert list_divider(POS_NEG_LISTS, [UNKNOWN_LIST]) == ([[5, 2],[6, 2]], [5])


def test_sentiment_value():
    assert sentiment(TOKENIZED_WORDS, WORDDICT) == [3]
    assert sentiment(EMPTY_LIST, WORDDICT) == -1
    assert sentiment(['is'], WORDDICT) == -1


def test_sentiment_analysis():
    assert sentiment_analysis(COMMENTSLIST, WORDDICT) == ([[7.5]], [[]])
    assert sentiment_analysis(EMPTY_LIST_LIST, WORDDICT) == ([[]], [[]])
    assert sentiment_analysis(NO_WORDS, WORDDICT) == ([[]], [[-1]])


def test_worddict():
    assert type(wordlist_to_dict()) == dict
    assert WORDDICT['happy'] == 8


def test_language_detector():
    assert LD.get_language('This is a lovely test for trying to figure out '
                           'the language.') == 'english'
    assert LD.get_language('Dette er en skøn test for at forsøge at finde ud '
                           ' af hvilket sprog det er') == 'danish'
    assert LD.get_language('C\'est un excellent metode pour détecter quelle '
                           ' langue il est!') == 'french'

#py.test test_sentiment.py
