# -*- coding: utf-8 -*-
"""Modules used to plot pie chart and histogram regarding sentiment."""
import matplotlib.pylab as plt
import matplotlib
import mpld3
# import numpy
# import random
# from time import sleep


def pie_chart(fractions_list):
    """
    Plotting a piechart of input.

    Keyword arguments:
    fractions_list -- list of two components; positive and negative counts.
    """
    labels = ['Positive', 'Negative']
    colors = ['#4CAF50', '#F44336']
    matplotlib.rcParams['text.color'] = '#263238'
    matplotlib.rcParams['lines.linewidth'] = 2
    matplotlib.rcParams['patch.edgecolor'] = 'white'
    matplotlib.rcParams['font.style'] = 'oblique'
    matplotlib.rcParams['font.size'] = 12

    fig = plt.figure()

    ax1 = fig.add_subplot(1, 2, 1)
    if fractions_list[0] == [0, 0]:
        ax1.text(0.1, 0.5, 'There is no plot to display', fontsize=20,
                 color='#263238')
    else:
        _, texts, _ = ax1.pie(fractions_list[0], labels=labels,
                              autopct='%1.1f%%', colors=colors)
        ax1.axis('equal')
        texts[0].set_fontsize(0)
        texts[1].set_fontsize(0)
        ax1.set_title('Sentiment Score')
        ax1.set_axis_off()
        ax1.legend()

    ax2 = fig.add_subplot(1, 2, 2)
    if fractions_list[1] == [0, 0]:
        ax2.text(0.1, 0.5, 'There is no plot to display', fontsize=20,
                 color='#263238')
    else:
        _, texts, _ = ax2.pie(fractions_list[1], labels=labels,
                              autopct='%1.1f%%', colors=colors)
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

    fig = plt.figure()

    ax = fig.add_subplot(1, 1, 1)
    ax.set_title('Histogram displaying Sentiment Bins')
    ax.set_xlabel('Bins')
    ax.set_ylabel('Comment Count')
    ax.set_xticks(bins[:-1])

    if sentiment_list == []:
        ax.text(3, 0.5, 'There is no plot to display', fontsize=25,
                color='#263238')
    else:
        n, bins, patches = ax.hist(sentiment_list, bins=bins, normed=1,
                                   histtype='bar', rwidth=0.6, stacked=True,
                                   align='left')

        for bin_, patch in zip(bins, patches):
            if bin_ > 6:
                patch.set_facecolor('#4CAF50')
                patch.set_label('Positive')
            elif bin_ <= 6:
                patch.set_facecolor('#F44336')
                patch.set_label('Negative')

    fig.tight_layout()
    plt.xticks(bins)

    return fig


def generate_pie_plots(sentiment_list, rating_list):
    """Given list of sentiments and a list of ratings, generate pie charts."""
    plot_list = []
    for sentiment, rating in zip(sentiment_list, rating_list):
        print [sentiment, rating]
        fig = pie_chart([sentiment, rating])
        # plot_list.append(fig)
        plot_list.append(mpld3.fig_to_html(fig))
    return plot_list


def genereate_hist_plots(sentiment_list):
    """Given a sentiment list, generate plots."""
    plot_list = []
    bins = range(1, 13)
    for sentiment in sentiment_list:
        fig = hist_graph(sentiment, bins)
        # plot_list.append(fig)
        plot_list.append(mpld3.fig_to_html(fig))
    return plot_list


def pos_neg_counter(sentiment_list):
    """Count the positive/negative comments in a list."""
    pos = len([sent for sent in sentiment_list if sent > 6 and sent <= 12])
    neg = len([sent for sent in sentiment_list if sent <= 6 and sent >= 0])
    return [pos, neg]


def list_divider(nested_list):
    """Input mapped based on pos_neg_counter function."""
    return map(pos_neg_counter, nested_list)


def main():
    """Manual testing of all internal methods."""
    # #Testing pie chart
    # scores1 = numpy.ones(50)
    # sent_score1 = [random.randrange(0, 13, 1) for _ in scores1]
    # scores2 = numpy.ones(50)
    # sent_score2 = [random.randrange(0, 13, 1) for _ in scores2]

    # #Testing hist graph
    # scores3 = numpy.ones(2)
    # rat_score1 = [random.randrange(0, 13, 1) for _ in scores3]
    # scores4 = numpy.ones(2)
    # rat_score2 = [random.randrange(0, 13, 1) for _ in scores4]

    # lal_list = []
    # lal_list.append(sent_score1)
    # lal_list.append(sent_score2)
    # sentiment_list = list_divider(lal_list)

    # rating_list = []
    # rating_list.append(rat_score1)
    # rating_list.append(rat_score2)

    # pie_chart_list = generate_pie_plots(sentiment_list, rating_list)
    # for chart in pie_chart_list:
    #     chart.show()
    #     sleep(2)

    # hist_plot_list = genereate_hist_plots(lal_list)
    # print lal_list
    # for plot in hist_plot_list:
    #     plot.show()
    #     sleep(5)

if __name__ == '__main__':
    main()
