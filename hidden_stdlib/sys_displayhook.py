#!/usr/bin/env python
# encoding: utf-8
"""Counting expression values.
"""

import sys

class ExpressionCounter(object):

    def __init__(self):
        self.count = 0
        self.history = []

    def __call__(self, value):
        if not self.history or value != self.history[-1]:
            self.count += 1
            sys.ps1 = '(%d)> ' % self.count
            self.history.append(value)
        sys.__displayhook__(value)

print 'installing expression counter'
sys.displayhook = ExpressionCounter()
