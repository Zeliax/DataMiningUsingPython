# -*- coding: utf-8 -*-
import pylab
import random

sent_score = random.sample(range(-6, 6), 20)


def main():
    neutral, positive, negative = []

    for nr in sent_score:
        if nr == 0:
            neutral.append(nr)
        elif nr > 0:
            positive.append(nr)
        elif nr < 0:
            negative.append(nr)

if __name__ == '__main__':
    main()
