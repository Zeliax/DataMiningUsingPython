# -*- coding: utf-8 -*-
"""Modules used to plot pie chart and histogram regarding sentiment."""
import matplotlib.pylab as plt
import matplotlib
import mpld3


def pie_chart(sentiment_list, rating_list, unknown_nr):
    """
    Plotting a piechart of input.

    Keyword arguments:
    fractions_list -- list of two components; positive and negative counts.
    """

    #Calculate differences in sentiment and likes/dislikes
    # sent_pos_amount = sentiment_list[0]
    # sent_neg_amount = sentiment_list[2]
    # rate_pos_amount = rating_list[0]
    # rate_neg_amount = rating_list[1]

    labels = ['Positive', 'Negative']
    colors = ['#4CAF50', '#F44336']

    matplotlib.rcParams['text.color'] = '#263238'
    matplotlib.rcParams['lines.linewidth'] = 2
    matplotlib.rcParams['patch.edgecolor'] = 'white'
    matplotlib.rcParams['font.style'] = 'oblique'
    matplotlib.rcParams['font.size'] = 12

    fig = plt.figure(figsize=[6, 6])

    nr_of_unknown_string = unknown_nr + 'unknown comments'

    ax1 = fig.add_subplot(1, 2, 1)
    if sentiment_list == [0, 0, 0]:
        ax1.text(0.1, 0.5,
                 'There is no plot to display',
                 fontsize=18,
                 color='#263238')
    else:
        _, texts, _ = ax1.pie(sentiment_list,
                              labels=labels,
                              autopct='%1.1f%%',
                              colors=colors)
        ax1.axis('equal')
        texts[0].set_fontsize(0)
        texts[1].set_fontsize(0)
        ax1.set_title('Sentiment Score')
        ax1.set_axis_off()
        ax1.legend()
        ax1.text(0.1, 0.1,
                 nr_of_unknown_string,
                 fontsize=12,
                 color='#263238')

    ax2 = fig.add_subplot(1, 2, 2)
    if rating_list == [0, 0, 0]:
        ax2.text(0.1, 0.5,
                 'There is no plot to display',
                 fontsize=20,
                 color='#263238')
    else:
        _, texts, _ = ax2.pie(rating_list,
                              labels=labels,
                              autopct='%1.1f%%',
                              colors=colors)
        ax2.axis('equal')
        texts[0].set_fontsize(0)
        texts[1].set_fontsize(0)
        ax2.set_title('Likes/Dislikes')
        ax2.set_axis_off()
        ax2.legend()

    fig.tight_layout()

    return fig


def hist_graph(sentiment_list, bins):
    """Method for plotting a historgraph of input.

    Keyword arguments:
    interval_list -- list of sentiment scores; scores between 0-12.
    """
    matplotlib.rcParams['text.color'] = '#263238'
    matplotlib.rcParams['lines.linewidth'] = 2
    matplotlib.rcParams['patch.edgecolor'] = 'white'
    matplotlib.rcParams['font.style'] = 'oblique'
    matplotlib.rcParams['font.size'] = 12

    fig = plt.figure(figsize=[6, 6])

    subfig = fig.add_subplot(1, 1, 1)
    subfig.set_title('Histogram displaying Sentiment Bins')
    subfig.set_xlabel('Bins')
    subfig.set_ylabel('Comment Count')
    subfig.set_xticks(bins[:-1])

    if sentiment_list == []:
        subfig.text(3, 0.5,
                    'There is no plot to display',
                    fontsize=20,
                    color='#263238')
    else:
        _, bins, patches = subfig.hist(sentiment_list,
                                       bins=bins,
                                       normed=1,
                                       histtype='bar',
                                       rwidth=0.6,
                                       stacked=True,
                                       align='left')

        for bin_, patch in zip(bins, patches):
            if bin_ >= 7:
                patch.set_facecolor('#4CAF50')
                patch.set_label('Positive')
            elif bin_ >= 6 and bin_ < 7:
                patch.set_facecolor('#FFC107')
                patch.set_label('Neutral')
            elif bin_ < 6:
                patch.set_facecolor('#F44336')
                patch.set_label('Negative')

    fig.tight_layout()
    plt.xticks(bins[:-1])

    return fig


def generate_pie_plots(sentiment_list, rating_list, unknown_nr):
    """Given list of sentiments and a list of ratings, generate pie charts."""
    plot_list = []
    for sentiment, rating in zip(sentiment_list, rating_list):
        fig = pie_chart(sentiment, rating, unknown_nr)
        plot_list.append(mpld3.fig_to_html(fig))
    return plot_list


def genereate_hist_plots(sentiment_list, bins):
    """Given a sentiment list, generate plots."""
    plot_list = []
    for sentiment in sentiment_list:
        fig = hist_graph(sentiment, bins)
        plot_list.append(mpld3.fig_to_html(fig))
    return plot_list


def unknown_list_counter(unknown_list):
    """ """
    unknowns = len([unknown for unknown in unknown_list])
    return unknowns


def pos_neg_counter(sentiment_list):
    """Count the positive/negative comments in a list."""
    positive = len([sent for sent in sentiment_list if sent > 6])
    negative = len([sent for sent in sentiment_list if sent <= 6])
    return [positive, negative]


def list_divider(nested_list, unknown_list):
    """Input mapped based on pos_neg_counter function."""
    print 'Nested list = ', nested_list
    print 'Uknown list = ', unknown_list
    pos_neg_count = map(pos_neg_counter, nested_list)
    unknown_nr = unknown_list_counter(unknown_list)
    return pos_neg_count, unknown_nr
