#!/usr/bin/env python
# encoding: utf-8
"""Using try:except to handle errors
"""

import sys

def main():
    try:
        # do some work
        raise RuntimeError('Helpful error message')
    except Exception as err:
        sys.stderr.write('ERROR: %s\n' % err)

if __name__ == '__main__':
    main()