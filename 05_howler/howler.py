#!/usr/bin/env python3
"""
Author : whisperer <whisperer@localhost>
Date   : 2024-02-17
Purpose: Howler (upper-cases input)
"""

import argparse
import os


def get_args():
    parser = argparse.ArgumentParser(
        description="Howler (upper-cases input)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('text', help='Input string or file')
    parser.add_argument('-o',
                        '--outfile',
                        metavar='str',
                        type=str,
                        help='Output filename',
                        default='')
    parser.add_argument('-l',
                        '--lower', help="Lower the input text", action='store_true')
    return parser.parse_args()


def main():
    args = get_args()
    word = args.text
    out = args.outfile
    lower1 = args.lower

    if os.path.isfile(word):
        word = open(word).read().upper().rstrip()
        if lower1:
            print(word.lower())
        else:
            print(word)
    elif out:
        fh = open(out, 'wt')
        fh.write(word.upper().rstrip())
        fh.close()
    elif lower1:
        print(word.lower())
    else:
        print(word.upper())



# --------------------------------------------------
if __name__ == '__main__':
    main()
