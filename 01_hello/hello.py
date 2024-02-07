#!/usr/bin/env python3
# Purpose: Say Hello
import argparse

def get_args():
    parser = argparse.ArgumentParser(description="Say Hello")
    parser.add_argument('-n', '--name', help="Name to greet", metavar='name', default='World')
    return parser.parse_args()



def main():
    args = get_args()
    print('Hello, ' + args.name + '!')

if __name__ == '__main__':
    main()