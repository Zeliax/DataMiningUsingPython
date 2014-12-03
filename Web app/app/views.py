from flask import render_template, flash, redirect, request, make_response, g
from app import app
from .forms import SearchForm
from YouTubeConnection import YouTubeConnection
from sentimentAnalysis import sentiment_analysis, wordlist_to_dict, sentiment
from Plotter import list_divider, pie_chart, generate_pie_plots, genereate_hist_plots
import config
import requests

developer_key = config.DEVELOPER_KEY
youtube_api_version = config.YOUTUBE_API_VERSION
youtube_api_service_name = config.YOUTUBE_API_SERVICE_NAME
ytc = YouTubeConnection(developer_key, youtube_api_version,
                        youtube_api_service_name)


@app.route('/')  # URL-path to homepage
@app.route('/index')
def index():
    """Define data for index.html.
    A title and a paragraph is send through the template to the index.html.
    """
    title = 'Youtube Sentiment Analysis'  # setting the title
    paragraph = "Welcome!"
    return render_template('index.html',
                           title=title,
                           paragraph=paragraph)


@app.route('/search', methods=['GET', 'POST'])
def search():
    """Define data for search.html.

    The form is defined. Data from the form is used to retrieve lists of
    comments, names, links and embedded through YouTubeConnection.
    Then it retrieve a sentiment score list from sentiment_analysis.
    A list of ratings from get_video_rating and to lists of html strings from
    generate_plot_list.

    All the lists is zipped and send through the template to the search.html.
    """
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
        no_of_results = 1
        search_word = request.form['search_word']
        no_of_results = request.form['no_of_results']
        commentlist, names, links, embedded = ytc.main_func(search_word,
                                                            no_of_results)
        sentiment = sentiment_analysis(commentlist, word_dict)
        ratings = ytc.get_video_rating(links)
        pos_neg = list_divider(sentiment)
        plot_list = generate_pie_plots(pos_neg, ratings)
        hist_plot_list = genereate_hist_plots(pos_neg)
        zipped = zip(names, embedded, plot_list, hist_plot_list)
        flash('Search requested for "%s"' % (search_word))
        return render_template('search.html',
                               form=form,
                               zipped=zipped)
    return render_template('search.html',
                           form=form,
                           zipped=zipped)
