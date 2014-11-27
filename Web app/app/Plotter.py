# -*- coding: utf-8 -*-
import matplotlib.pylab as plt
import matplotlib
import random
import numpy

from time import sleep


def pie_chart(fractions_list):
    """
    Function for plotting a piechart of sentiment analysis of YouTube videos.

    Function takes in a list of fractions and a list of labels and plots a pie
    chart based on that.
    """
    labels = 'Positive', 'Negative'
    colors = ('g', 'r')
    matplotlib.rcParams['text.color'] = 'white'
    matplotlib.rcParams['lines.linewidth'] = 2
    matplotlib.rcParams['patch.edgecolor'] = 'white'
    matplotlib.rcParams['font.style'] = 'oblique'
    matplotlib.rcParams['font.size'] = 18

    fig = plt.figure()
    for i in xrange(1, 3):
        plt.subplot(220 + i)
        plt.pie(fractions_list[i - 1], labels=labels, autopct='%1.1f%%',
                colors=colors)

    fig.subplots_adjust(hspace=1)
    return fig


def hist_graph():
    print "Hello"


def pos_neg_counter(sent_list):
    pos = len([sent for sent in sent_list if sent >= 6 and sent <= 12])
    neg = len([sent for sent in sent_list if sent < 6 and sent >= 0])
    return [pos, neg]


def list_divider2(list_list):
    new_list = []
    for a_list in list_list:
        new_list.append(pos_neg_counter(a_list))
    return new_list


def list_divider1(list_list):
    return map(pos_neg_counter, list_list)


def generate_subplot_2d(plot_list, plot_names):
    print "Hello"


def main():
    scores1 = numpy.ones(50)
    sent_score1 = [random.randrange(0, 12, 1) for _ in scores1]
    scores2 = numpy.ones(50)
    sent_score2 = [random.randrange(0, 12, 1) for _ in scores2]
    # scores3 = numpy.ones(50)
    # sent_score3 = [random.randrange(0, 12, 1) for nr in scores3]
    # scores4 = numpy.ones(50)
    # sent_score4 = [random.randrange(0, 12, 1) for nr in scores4]

    # scores5 = numpy.ones(50)
    # sent_score5 = [random.randrange(0, 12, 1) for nr in scores5]
    # scores6 = numpy.ones(50)
    # sent_score6 = [random.randrange(0, 12, 1) for nr in scores6]

    lal_list = []
    lal_list.append(sent_score1)
    lal_list.append(sent_score2)
    # lal_list.append(sent_score3)
    # lal_list.append(sent_score4)

    test_list = [[0.52631578947368418, 0.0, 0.25, 0.94736842105263153,
                  0.90000000000000002, 0.0, 1.25, 0.6428571428571429,
                  0.81818181818181823, 0.0, 0.25, 1.125, 0.21052631578947367,
                  0.26666666666666666, 0.0, 0.27272727272727271,
                  0.27272727272727271, 1.2727272727272727, 0.0,
                  1.2857142857142858, 0.0, 0.1875, 1.0, 0.0, 1.0, 1.5,
                  0.88888888888888884, 1.588235294117647, 0.26436781609195403,
                  0.5625, 1.0769230769230769, 0.5, 1.8, 1.0, 2.0,
                  0.27272727272727271, 0.27272727272727271,
                  0.27272727272727271],
                 [0.52631578947368418, 0.0, 0.25, 0.94736842105263153,
                  0.90000000000000002, 0.0, 1.25, 0.6428571428571429,
                  0.81818181818181823, 0.0, 0.25, 1.125, 0.21052631578947367,
                  0.26666666666666666, 0.0, 0.27272727272727271,
                  0.27272727272727271, 1.2727272727272727, 0.0,
                  1.2857142857142858, 0.0, 0.1875, 1.0, 0.0, 1.0, 1.5,
                  0.88888888888888884, 1.588235294117647, 0.26436781609195403,
                  0.5625, 1.0769230769230769, 0.5, 1.8, 1.0, 2.0,
                  0.27272727272727271, 0.27272727272727271,
                  0.27272727272727271]]

    # print lal_list

    #Mette from here
    fractions_list = list_divider1(test_list)
    # fractions_list = list_divider2(lal_list)

    print fractions_list

    chart = pie_chart(fractions_list)
    chart.show()
    sleep(2)

    # pie_chart(fractions_list, plot_names)

if __name__ == '__main__':
    main()
