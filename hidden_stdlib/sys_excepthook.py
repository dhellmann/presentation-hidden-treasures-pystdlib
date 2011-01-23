#!/usr/bin/env python
# encoding: utf-8
"""Replace the default system exception handler.
"""

import sys

def quiet_errors(exc_type, exc_value, traceback):
    sys.stderr.write('ERROR: %s\n' % exc_value)

sys.excepthook = quiet_errors

raise RuntimeError('Error message goes here')
