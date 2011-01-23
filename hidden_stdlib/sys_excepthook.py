#!/usr/bin/env python
# encoding: utf-8
"""Replace the default system exception handler.
"""

import sys

def quiet_errors(exc_type, exc_value, traceback):
    sys.stderr.write('ERROR: %s\n' % exc_value)

sys.excepthook = quiet_errors

def main():
    # do some work
    raise RuntimeError('Error message goes here')

if __name__ == '__main__':
    main()
