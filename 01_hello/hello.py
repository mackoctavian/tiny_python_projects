#!/usr/bin/env python3
"""
Author: Mack Octavian <maestrooctavian@gmail.com"
Purpose: Say Hello
"""
import argparse


def get_args():
    """Get the command-line arguments """

    parser = argparse.ArgumentParser(description="Say Hello")
    parser.add_argument('-n',
                        '--name',
                        help="Name to greet",
                        metavar='name',
                        default='World')
    return parser.parse_args()


def main():
    """Make a jazz noise here"""

    args = get_args()
    print('Hello, ' + args.name + '!')


if __name__ == '__main__':
    main()
