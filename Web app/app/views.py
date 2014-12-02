from flask import render_template, flash, redirect, request, make_response, g
from app import app
from .forms import SearchForm
from YouTubeConnection import YouTubeConnection
from sentimentAnalysis import sentiment_analysis, wordlist_to_dict, sentiment
from Plotter import list_divider, pie_chart, generate_plot_list
import config
import requests

developer_key = config.DEVELOPER_KEY
youtube_api_version = config.YOUTUBE_API_VERSION
youtube_api_service_name = config.YOUTUBE_API_SERVICE_NAME
ytc = YouTubeConnection(developer_key, youtube_api_version, youtube_api_service_name)

@app.route('/')  # URL-path to homepage
@app.route('/index')
def index():
    """Calculates the mean sentiment of each comment.

    Keyword arguments:
    commentlist -- a list of lists of comments
    """
    title='Youtube Sentiment Analysis' #setting the title
    paragraph = "Welcome!"
    return render_template('index.html',
                           title=title,
                           paragraph=paragraph)


@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    commentlist = []
    sentiment = []
    names = []
    links = []
    zipped = []
    zip_plots = []
    pos_neg = []
    ratings = []
    plot_list = []
    embedded = []
    word_dict = wordlist_to_dict()
    if form.validate_on_submit():
        nr_of_results = 1
        search_word = request.form['search_word']
        nr_of_results = request.form['nr_of_results']
        commentlist, names, links, embedded = ytc.main_func(search_word, nr_of_results)
        assert commentlist
        sentiment = sentiment_analysis(commentlist, word_dict)
        ratings = ytc.get_video_rating(links)
        assert ratings
        pos_neg = list_divider(sentiment)
        plot_list, hist_plot_list = generate_plot_list(pos_neg, ratings)
        zipped = zip(names, embedded, plot_list, hist_plot_list)
        flash('Search requested for "%s"' %
        (search_word))
        return render_template('search.html',
                           form=form,
                           sentiment=sentiment,
                           commentlist=commentlist,
                           zipped=zipped,
                           pos_neg=pos_neg,
                           links=links,
                           ratings=ratings,
                           embedded=embedded)
    return render_template('search.html',
                           form=form,
                           sentiment=sentiment,
                           commentlist=commentlist,
                           zipped=zipped,
                           pos_neg=pos_neg,
                           links=links,
                           ratings=ratings,
                           embedded=embedded)