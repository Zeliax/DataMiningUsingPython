# -*- coding: utf-8 -*-
import matplotlib.pylab as plt
import matplotlib
# import random
# import numpy


def pie_chart(fraction, labels):
    """
    Function for plotting a piechart of sentiment analysis of YouTube videos.

    Function takes in a list of fractions and a list of labels and plots a pie
    chart based on that.
    """
    colors = ('g', 'r')
    matplotlib.rcParams['text.color'] = 'white'
    matplotlib.rcParams['lines.linewidth'] = 2
    matplotlib.rcParams['patch.edgecolor'] = 'white'
    matplotlib.rcParams['font.style'] = 'oblique'
    matplotlib.rcParams['font.size'] = 18
    plt.figure(1, figsize=(10, 10))
    plt.pie(fraction, labels=labels, colors=colors, autopct='%.0f%%')
    plt.show()

# if __name__ == '__main__':
    #Testing the pie chart
    # scores = numpy.ones(50)
    # sent_score = [random.randrange(-6, 6, 1) for nr in scores]

    # positive = []
    # negative = []
    # fraction = []

    # for nr in sent_score:
    #     if nr > 0:
    #         positive.append(nr)
    #     elif nr <= 0:
    #         negative.append(nr)

    # fraction.append(len(sent_score) / len(positive))
    # fraction.append(len(sent_score) / len(negative))

    # labels = 'Positive', 'Negative'

    # pie_chart(fraction, labels)
