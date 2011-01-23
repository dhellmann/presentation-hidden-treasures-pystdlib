#!/usr/bin/env python
# encoding: utf-8
""" Define a class to be encoded.
"""

class MyObj(object):
    def __init__(self, s):
        self.s = s
    def __repr__(self):
        return '<MyObj(%s)>' % self.s
