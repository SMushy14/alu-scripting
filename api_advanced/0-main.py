#!/usr/bin/python3
"""Main script to test number_of_subscribers function"""
import sys
from 0-subs import number_of_subscribers

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <subreddit>".format(sys.argv[0]))
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))

