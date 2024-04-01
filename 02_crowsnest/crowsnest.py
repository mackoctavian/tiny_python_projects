#!/usr/bin/env python3
"""
Author : Mack Octavian <maestrooctavian@gmail.com>
Date   : 2024-02-07
Purpose: Rock the Casbah
"""

import argparse


def get_args():
    parser = argparse.ArgumentParser(description='Rock the Casbah')
    parser.add_argument('word', metavar='word', help='A word')
    return parser.parse_args()

def main():
    args = get_args()
    word = args.word
    article = 'an' if word[0].lower() in 'aeiou' else 'a'
    print(f'Ahoy, Captain, {article} {word} off the larboard bow!')  

if __name__ == '__main__':
    main()