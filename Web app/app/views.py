from flask import render_template, flash, redirect
from app import app
from .forms import SearchForm
from .YouTubeVideoComments import main

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
    if form.validate_on_submit():
        flash('Search requested for "%s"' %
              (form.search_word.data))
        return redirect('/search')

    search_word = form.search_word.data
    nr_of_results = 3
    main_func(search_word, nr_of_results)
    return render_template('search.html',
                           form=form)