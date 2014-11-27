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

    # print lal_list

    #Mette from here
    fractions_list = list_divider2(lal_list)

    print fractions_list

    # for fraction in fractions_list:
    # chart = pie_chart(fractions_list)
    # chart.show()
    # sleep(2)

    # pie_chart(fractions_list, plot_names)

if __name__ == '__main__':
    main()
