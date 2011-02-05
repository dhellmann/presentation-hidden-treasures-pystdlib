#!/usr/bin/env python
# encoding: utf-8
"""Demonstrate default error handler.
"""

def main():
    # do some work
    raise RuntimeError('Helpful error message')

if __name__ == '__main__':
    main()