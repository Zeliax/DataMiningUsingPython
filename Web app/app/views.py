from flask import render_template, flash, redirect, request
from app import app
from .forms import SearchForm
from YouTubeConnection import main_func
from sentimentAnalysis import sentiment_analysis, wordlist_to_dict, sentiment

@app.route('/') #URL-path to homepage
@app.route('/index')
def index():
	title='Youtube Sentiment Analysis' #setting the title
	paragraph = "Welcome!"
	return render_template('index.html',
                           title=title,
                           paragraph=paragraph)
@app.route('/comments')
def comment():
	title='Comments' #setting the title
	comments = ["comment1", "comment2", "comment3", "comment4"]
	return render_template('comments.html',
                           title=title,
                           comments=comments)

@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    commentlist = []
    sentiment = []
    names = []
    links = []
    zipped = []
    words = ["but", "he", "fails", "miserably"]
    word_dict = wordlist_to_dict(r'C:\Users\Mette\Documents\GitHub\DataMiningUsingPython\Web app\app\FINN-wordlist.txt')
    if form.validate_on_submit():
        search_word = form.search_word.data
        nr_of_results = request.form['nr_of_results']
        commentlist, names, links = main_func(search_word, nr_of_results)
        assert commentlist
        sentiment = sentiment_analysis(commentlist,word_dict)
        zipped = zip(commentlist, sentiment)
        flash('Search requested for "%s"' %
        (search_word))
        return render_template('search.html',
                           form=form,
                           sentiment=sentiment,
                           commentlist=commentlist,
                           names=names,
                           links=links,
                           zipped=zipped)
    return render_template('search.html',
                           form=form,
                           sentiment=sentiment,
                           commentlist=commentlist,
                           names=names,
                           links=links,
                           zipped=zipped)