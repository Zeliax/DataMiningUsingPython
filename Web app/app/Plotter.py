# -*- coding: utf-8 -*-
import matplotlib.pylab as plt
import matplotlib
import random
import numpy

from time import sleep


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
        plt.subplot(220 + i)
        plt.pie(fractions_list[i - 1], labels=labels, autopct='%1.1f%%',
                colors=colors)

    fig.subplots_adjust(hspace=1)
    return fig


def hist_graph(interval_list):
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

    bins = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    n, bins, patches = plt.hist(interval_list, bins, normed=1, histtype='bar',
                                rwidth=0.8, stacked=True)
    plt.setp(patches, 'facecolor', 'b', 'alpha', 0.75)

    return fig


def pos_neg_counter(sent_list):
    """Method that counts the positive/negative comments in a list."""
    pos = len([sent for sent in sent_list if sent >= 6 and sent <= 12])
    neg = len([sent for sent in sent_list if sent < 6 and sent >= 0])
    return [pos, neg]


def list_divider1(list_list):
    """Input is mapped based on pos_neg_counter function."""
    return map(pos_neg_counter, list_list)


def list_divider2(list_list):
    """Manual mapping of input based on pos_neg_counter function."""
    new_list = []
    for a_list in list_list:
        new_list.append(pos_neg_counter(a_list))
    return new_list


def main():
    """Manual testing of all internal methods"""
    #Testing pie chart
    # scores1 = numpy.ones(50)
    # sent_score1 = [random.randrange(0, 12, 1) for _ in scores1]
    # scores2 = numpy.ones(50)
    # sent_score2 = [random.randrange(0, 12, 1) for _ in scores2]

    # lal_list = []
    # lal_list.append(sent_score1)
    # lal_list.append(sent_score2)

    # fractions_list = list_divider1(lal_list)

    # chart = pie_chart(fractions_list)
    # chart.show()

    #Testing histogram
    ones_list = numpy.ones(50)
    interval_list = [random.randrange(0, 12, 1) for _ in ones_list]

    hist = hist_graph(interval_list)
    hist.show()
    sleep(2)

if __name__ == '__main__':
    main()
