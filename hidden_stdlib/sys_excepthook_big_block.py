#!/usr/bin/env python
# encoding: utf-8
"""Demonstrate default error handler.
"""

import sys

def main():
    try:
        # do some work
        raise RuntimeError('Error message goes here')
    except Exception as err:
        sys.stderr.write('ERROR: %s\n', err)

if __name__ == '__main__':
    main()
