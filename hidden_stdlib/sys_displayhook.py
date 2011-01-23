#!/usr/bin/env python
# encoding: utf-8
"""Counting expression values.
"""

import sys

class ExpressionCounter(object):

    def __init__(self):
        self.count = 0
        self.previous_value = self

    def __call__(self, value):
        if value != self.previous_value:
            self.count += 1
            sys.ps1 = '(%d)> ' % self.count
        self.previous_value = value
        sys.__displayhook__(value)

sys.displayhook = ExpressionCounter()
