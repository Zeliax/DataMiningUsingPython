# -*- coding: utf-8 -*-
import matplotlib.pylab as plt
import matplotlib
# import random
# import numpy
from collections import Counter


def pie_chart(fraction):
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
    plt.figure(1, figsize=(10, 10))
    plot = plt.pie(fraction, labels=labels, colors=colors, autopct='%.0f%%')
    # plt.show()
    return plot

def bar_graph():
    print "Hello"


def pos_neg_counter(sent_list):
    fraction = []
    lists = []
    for s_list in sent_list:
        count = Counter(s_list)
        fraction.append(sum([value for key, value in count.items() if key >= 0 and
                             key <= 6]))
        fraction.append(sum([value for key, value in count.items() if key < 0 and
                             key >= -6]))
        lists.append(fraction)

    return lists


if __name__ == '__main__':
    print "Hello"
    #Testing the pie chart
    # scores = numpy.ones(50)
    # sent_score = [random.randrange(-6, 6, 1) for nr in scores]

    # fraction = pos_neg_counter(sent_score)

    # pie_chart(fraction)
