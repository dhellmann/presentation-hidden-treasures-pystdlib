#!/usr/bin/env python
# encoding: utf-8
"""Quoting command line arguments to build shell commands.
"""

import pipes

raw = [ 'ls', 'with space', 
        '"already quoted"',
        "with ' embedded", ]
print 'RAW  :', ' '.join(raw)

cmd = ' '.join(pipes.quote(a) for a in raw)
print 'QUOTE:', cmd