#!/usr/bin/env python
# encoding: utf-8
"""Demonstrate default error handler.
"""

import sys

def main():
    # do some work
    raise RuntimeError('Error message goes here')

if __name__ == '__main__':
    main()
    
