#! /usr/bin/env python

import sys
import random
from datetime import datetime


def random_adjective():
    adjectives = ['beautiful', 'nice', 'hairy', 'mean', 'scary', 'poopy', 'deaf',
                  'blind', 'intelligent', 'sweet', 'smelly', 'happy', 'sad', 'helpless',
                  'wet', 'dry', 'angry', 'noisy', 'quiet', 'crowded', 'freckled',
                  'dingy', 'quick', 'slow', 'blond', 'tall', 'small']

    return random.choice(adjectives)


def mad_libs(argv):
    while True:
        username = raw_input('Enter your name, please: ')

        if username == 'quit':
            break

        print "You are very " + random_adjective() + ", " + username


if __name__ == "__main__":
    random.seed(datetime.now())

    mad_libs(sys.argv[1:])
