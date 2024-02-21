#!/usr/bin/env python3
"""
Author : whisperer <whisperer@localhost>
Date   : 2024-02-17
Purpose: Howler (upper-cases input)
"""

import argparse
import os


def get_args():
    parser = argparse.ArgumentParser(description="Howler (upper-cases input)", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('text',  help='Input string or file')
    parser.add_argument('-o',
                        '--outfile',
                        metavar='str',
                        type=str,
                        help='Output filename',
                        default='')

    return parser.parse_args()


def main():
    args = get_args()
    word = args.text
    out = args.outfile

    if os.path.isfile(word):
        word = open(word).read().upper().rstrip()
        print(word)
    elif out:
        fh = open(out, 'wt')
        fh.write(word.upper().rstrip())
        fh.close()
    else:
        print(word.upper())



# --------------------------------------------------
if __name__ == '__main__':
    main()
