# -*- coding: utf-8 -*-
import matplotlib.pylab as plt
import matplotlib
import random
import numpy
import time


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
    plot = plt.figure(1, figsize=(10, 10))
    plt.pie(fraction, labels=labels, colors=colors, autopct='%.0f%%')
    return plot


def hist_graph():
    print "Hello"


def pos_neg_counter(sent_list):
    pos = len([sent for sent in sent_list if sent >= 6 and sent <= 12])
    neg = len([sent for sent in sent_list if sent < 6 and sent >= 0])
    fraction = (pos, neg)
    return fraction


def list_divider(list_list):
    return map(pos_neg_counter, list_list)


def generate_subplot(plot_list, plot_names):
    for plot in plot_list:
        plot.show()


def plot_pies(lists):
    pie_charts = []
    for f_list in lists:
        pie_charts.append(pie_chart(f_list))
    return pie_charts


def main():
    scores1 = numpy.ones(50)
    sent_score1 = [random.randrange(0, 12, 1) for nr in scores1]
    scores2 = numpy.ones(50)
    sent_score2 = [random.randrange(0, 12, 1) for nr in scores2]

    lal_list = []
    lal_list.append(sent_score1)
    lal_list.append(sent_score2)

    #Mette from here
    fractions = list_divider(lal_list)
    print fractions

    for fraction in fractions:
        fig = pie_chart(fraction)
        fig.show()
    time.sleep(2)

if __name__ == '__main__':
    main()
