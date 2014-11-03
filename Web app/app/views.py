from flask import render_template, flash, redirect
from app import app
from .forms import SearchForm

@app.route('/')
# @app.route('/index')
# def index():
#     user = {'nickname': 'Mette'}  # fake user
#     posts = [  # fake array of posts
#         { 
#             'author': {'nickname': 'John'}, 
#             'body': 'Beautiful day in Portland!' 
#         },
#         { 
#             'author': {'nickname': 'Susan'}, 
#             'body': 'The Avengers movie was so cool!' 
#         }
#     ]
#     return render_template('index.html',
#                            title='Youtube Sentiment Analysis',
#                            user=user,
#                            posts=posts)

@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        flash('Search requested for "%s"' %
              (form.search_word.data))
        return redirect('/search')
    return render_template('search.html', 
                           title='Search',
                           form=form)