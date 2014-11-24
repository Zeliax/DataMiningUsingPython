#-*- coding: utf-8 -*-
import matplotlib.pylab as plt
# import matplotlib.pyplot as pplt
import matplotlib
# import io
# import Image
import random
import numpy

# from PIL import Image
from collections import Counter

LIST = open('FINN-wordlist.txt')


def pie_chart(fraction_list):
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

    fig = plt.figure(1, figsize=(10, 10))
    plt.pie(fraction_list, labels=labels, colors=colors, autopct='%.0f%%')
    return fig


def bar_graph():
    """
    Bla bla bla
    """
    print "Hello"


def pos_neg_counter(sent_list):
    """
    Counts the amount of negative and positive comments based on a sentiment
    list
    """
    fraction = []

    count = Counter(sent_list)
    fraction.append(sum([value for key, value in count.items() if key >= 0 and
                         key <= 6]))
    fraction.append(sum([value for key, value in count.items() if key < 0 and
                         key >= -6]))

    return fraction

# def main():
#     """
#     Main function to test code
#     """
#     scores = numpy.ones(50)
#     sent_score = [random.randrange(-6, 6, 1) for _ in scores]

#     fraction = pos_neg_counter(sent_score)

#     fig = pie_chart(fraction)

# if __name__ == '__main__':
#     main()
