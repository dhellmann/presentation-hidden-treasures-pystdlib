#!/usr/bin/env python
# encoding: utf-8
"""Splitting a command line into arguments.
"""

import shlex

for cmd in [ 
    r'''ls "hidden stdlib" "\"already quoted\"" "with ' embedded"''',  # subprocess
    """ls 'hidden stdlib' '"already quoted"' 'with '"'"' embedded'""", # pipes
    ]:
    print cmd
    print shlex.split(cmd)
    print
