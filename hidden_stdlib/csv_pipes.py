#!/usr/bin/env python
# encoding: utf-8
"""Pipe-delimited dialect for parsing sqlite3 output
"""

import csv
import sys

csv.register_dialect('pipes', delimiter='|')

reader = csv.reader(sys.stdin, dialect='pipes')
for row in reader:
    print row