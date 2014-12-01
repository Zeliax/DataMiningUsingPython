from flask import render_template, flash, redirect, request, make_response, g
from app import app
from .forms import SearchForm
from YouTubeConnection import YouTubeConnection
from sentimentAnalysis import sentiment_analysis, wordlist_to_dict, sentiment
from Plotter import list_divider, pie_chart
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
    pos_neg = []
    ratings = []
    # sentiment = [[7.5,6.6],[7.7,2.2]]
    word_dict = wordlist_to_dict()
    if form.validate_on_submit():
        nr_of_results = 1
        search_word = request.form['search_word']
        nr_of_results = request.form['nr_of_results']
        commentlist, names, links = ytc.main_func(search_word, nr_of_results)
        assert commentlist
        sentiment = sentiment_analysis(commentlist, word_dict)
        ratings = ytc.get_video_rating(links)
        assert ratings
        zipped = zip(names, links)
        flash('Search requested for "%s"' %
        (search_word))
        return render_template('search.html',
                           form=form,
                           sentiment=sentiment,
                           commentlist=commentlist,
                           zipped=zipped,
                           pos_neg=pos_neg,
                           links=links,
                           ratings=ratings)
    return render_template('search.html',
                           form=form,
                           sentiment=sentiment,
                           commentlist=commentlist,
                           zipped=zipped,
                           pos_neg=pos_neg,
                           links=links,
                           ratings=ratings)

@app.route("/plot.png", methods=['GET', 'POST'])
def plot():
    import datetime
    import StringIO
    import random
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter
    import matplotlib.pylab as plt
    import matplotlib

    # fig=Figure()
    # ax=fig.add_subplot(111)
    # x=[]
    # y=[]
    # now=datetime.datetime.now()
    # delta=datetime.timedelta(days=1)
    # for i in range(10):
    #     x.append(now)
    #     now+=delta
    #     y.append(random.randint(0, 1000))
    # ax.plot_date(x, y, '-')
    # ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    # fig.autofmt_xdate()
    plot = []
    sentiment = eval(request.args['sentiment'])
    plot = list_divider(zipped2)
    fig = pie_chart(plot)
    canvas = FigureCanvas(fig)
    png_output = StringIO.StringIO()
    canvas.print_png(png_output)
    response = make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'
    return response
