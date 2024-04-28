#!/usr/bin/env python3
"""
Author : whisperer <whisperer@localhost>
Date   : 2024-04-28
Purpose: Picnic Game
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic Game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('item',metavar='str', help='Item(s) to bring', nargs='+')
    parser.add_argument('-s', '--sorted', help='Sort the items', action='store_true')
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    item = ''
    arranged = args.sorted

    if arranged:
        args.item.sort()

    if len(args.item) > 2:
        args.item[-1] = 'and ' + args.item[-1]
        item = ', '.join(args.item)
    elif len(args.item) == 2:
        item = ' and '.join(args.item)
    else:
        item = ''.join(args.item)

   
    

    print(f'You are bringing {item}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
