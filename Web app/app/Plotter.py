# -*- coding: utf-8 -*-
"""Modules used to plot pie chart and histogram regarding sentiment."""
import matplotlib.pylab as plt
import matplotlib
import mpld3


def pie_chart(fractions_list):
    """
    Plotting a piechart of input.

    Keyword arguments:
    fractions_list -- list of two components; positive and negative counts.
    """
    labels = 'Positive', 'Negative'
    colors = ('g', 'r')
    matplotlib.rcParams['text.color'] = 'white'
    matplotlib.rcParams['lines.linewidth'] = 2
    matplotlib.rcParams['patch.edgecolor'] = 'white'
    matplotlib.rcParams['font.style'] = 'oblique'
    matplotlib.rcParams['font.size'] = 12

    fig = plt.figure()
    for i in xrange(1, 3):
        plt.subplot(1, 2, i)
        plt.pie(fractions_list[i - 1], labels=labels, autopct='%1.1f%%',
                colors=colors)

    fig.subplots_adjust(hspace=1)
    return fig


def hist_graph(sentiment_list, bins):
    """Method for plotting a historgraph of input.

    Keyword arguments:
    interval_list -- list of sentiment scores; scores between 0-12.
    """
    matplotlib.rcParams['text.color'] = 'white'
    matplotlib.rcParams['lines.linewidth'] = 2
    matplotlib.rcParams['patch.edgecolor'] = 'white'
    matplotlib.rcParams['font.style'] = 'oblique'
    matplotlib.rcParams['font.size'] = 12

    fig = plt.figure()

    n, bins, patches = plt.hist(sentiment_list, bins, normed=1, histtype='bar',
                                rwidth=0.8, stacked=True)
    plt.setp(patches, 'facecolor', 'b', 'alpha', 0.75)

    return fig


def generate_pie_plots(sentiment_list, rating_list):
    """Given list of sentiments and a list of ratings, generate pie charts."""
    plot_list = []
    for sentiment, rating in zip(sentiment_list, rating_list):
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
    neg = len([sent for sent in sentiment_list if sent < 6 and sent >= 0])
    return [pos, neg]


def list_divider(nested_list):
    """Input mapped based on pos_neg_counter function."""
    return map(pos_neg_counter, nested_list)


def main():
    """Manual testing of all internal methods."""
    #Testing pie chart
    # scores1 = numpy.ones(50)
    # sent_score1 = [random.randrange(0, 12, 1) for _ in scores1]
    # scores2 = numpy.ones(50)
    # sent_score2 = [random.randrange(0, 12, 1) for _ in scores2]
    #Testing hist graph
    # scores3 = numpy.ones(2)
    # rat_score1 = [random.randrange(0, 12, 1) for _ in scores3]
    # scores4 = numpy.ones(2)
    # rat_score2 = [random.randrange(0, 12, 1) for _ in scores4]

    # lal_list = []
    # lal_list.append(sent_score1)
    # lal_list.append(sent_score2)
    # sentiment_list = list_divider(lal_list)

    # rating_list = []
    # rating_list.append(rat_score1)
    # rating_list.append(rat_score2)

    # print lal_list

    # hist_plot_list = genereate_hist_plots(lal_list)
    # for plot in hist_plot_list:
    #     plot.show()
    #     sleep(2)

    # pie_chart_list = generate_pie_plots(sentiment_list, rating_list)
    # for chart in pie_chart_list:
    #     chart.show()
    #     sleep(2)

    # generate_plot_list(fractions_list, new_list)

    # chart = pie_chart(fractions_list)
    # chart.show()
    # sleep(2)

    #Testing histogram
    # ones_list = numpy.ones(50)
    # interval_list = [random.randrange(0, 12, 1) for _ in ones_list]

    # hist = hist_graph(interval_list)
    # hist.show()
    # sleep(2)

if __name__ == '__main__':
    main()
