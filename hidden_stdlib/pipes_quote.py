#!/usr/bin/env python
# encoding: utf-8
"""Quoting command line argument parts to build shell commands.
"""

import pipes

cmd = ' '.join(pipes.quote(a)
               for a in [ 'ls', 'hidden stdlib', '"already quoted"',
                          "with ' embedded", ])
print cmd

    


