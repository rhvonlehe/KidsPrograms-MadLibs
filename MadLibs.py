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

def random_noun():
    nouns = ['rock', 'man', 'car', 'woman', 'house', 'cabin',
             'windows', 'river', 'mouse', 'dog', 'computer',
             'cat', 'bigfoot', 'alien', 'balloon', 'circus',
             'piano', 'plant', 'whale', 'telephone pole',
             'fish', 'gremlin', 'bus', 'light switch', 'mole',
             'pimple', 'booger', 'fingernail', 'paint can' ]

    return random.choice(nouns)

def random_verbs_present_participle():
    verbs = ['running', 'walking', 'spitting', 'selling', 'buying',
             'reading', 'farting', 'herding', 'brushing', 'jumping', 'riding',
             'yelling', 'playing', 'talking', 'driving', 'writing', 'calling',
             'swimming', 'sleeping', 'feeding', 'eating', 'jumping', 'losing',
             'wandering', 'exploring']

    return random.choice(verbs)

def mad_libs(argv):
    while True:
        username = raw_input('Enter your name, please: ')

        if username == 'quit':
            break

        print username + " was " + random_verbs_present_participle() + \
            " when all of a sudden there appeared a " + \
            random_adjective() + " " + random_noun() + "."

        #print "You are very " + random_adjective() + ", " + username

if __name__ == "__main__":
    random.seed(datetime.now())

    mad_libs(sys.argv[1:])

