from flask import render_template, flash, redirect
from app import app
from .forms import SearchForm
from YouTubeConnection import main_func

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
    comment_list = []
    # temp_comment_list = []
    if form.validate_on_submit():
        search_word = form.search_word.data
        # for hver gang der trykkes på "search" skal søgeordet appendes en liste 
        nr_of_results = 1
        comment_list = main_func(search_word, nr_of_results)
        # temp_comment_list += main_func(search_word, nr_of_results)
        assert comment_list
        # for video_id, comment in comment_dict.iteritems():
        #     temp = []
        #     temp.extend([video_id])  #Note that this will change depending on the structure of your dictionary
        #     table.append(temp)
        flash('Search requested for "%s"' %
        (search_word))
        return render_template('search.html',
                           form=form,
                           comment_list=comment_list)
    return render_template('search.html',
                           form=form,
                           comment_list=comment_list)