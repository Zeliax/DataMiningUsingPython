from flask import render_template, flash, redirect, request, make_response
from app import app
from .forms import SearchForm
from YouTubeConnection import main_func
from sentimentAnalysis import sentiment_analysis, wordlist_to_dict, sentiment
from Plotter import pie_chart, pos_neg_counter

@app.route('/') #URL-path to homepage
@app.route('/index')
def index():
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
    pos_neg = []
    word_dict = wordlist_to_dict()
    if form.validate_on_submit():
        nr_of_results = 1
        search_word = request.form['search_word']
        nr_of_results = request.form['nr_of_results']
        commentlist, names, links = main_func(search_word, nr_of_results)
        assert commentlist
        sentiment = sentiment_analysis(commentlist,word_dict)
        # zipped = zip(commentlist, sentiment)
        pos_neg = pos_neg_counter(sentiment)
        flash('Search requested for "%s"' %
        (search_word))
        return render_template('search.html',
                           form=form,
                           sentiment=sentiment,
                           commentlist=commentlist,
                           names=names,
                           links=links,
                           zipped=zipped,
                           pos_neg=pos_neg)
    return render_template('search.html',
                           form=form,
                           sentiment=sentiment,
                           commentlist=commentlist,
                           names=names,
                           links=links,
                           zipped=zipped,
                           pos_neg=pos_neg)

@app.route("/simple.png")
def simple():
    import datetime
    import StringIO
    import random
 
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter
 
    fig=Figure()
    ax=fig.add_subplot(111)
    x=[]
    y=[]
    now=datetime.datetime.now()
    delta=datetime.timedelta(days=1)
    for i in range(10):
        x.append(now)
        now+=delta
        y.append(random.randint(0, 1000))
    ax.plot_date(x, y, '-')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    canvas=FigureCanvas(fig)
    png_output = StringIO.StringIO()
    canvas.print_png(png_output)
    response=make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'
    return response