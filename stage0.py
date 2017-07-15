#!/usr/bin/env python

from argparse import ArgumentParser
from slacker import Slacker
import sys


with open('.token', 'r') as f:
    token = f.read().strip()
print('\n--- Used token: {} ---\n'.format(token))
slack = Slacker(token)


def talk(blabber):
    slack.chat.post_message('#monitor', str(blabber))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('blabber',
                        help='let the bot talk blabber')
    args = parser.parse_args()
    if len(args.blabber) > 0:
        talk(args.blabber)
