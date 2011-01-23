#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2011 Doug Hellmann.  All rights reserved.
#
"""Quoting command line argument parts to build shell commands.
"""
#end_pymotw_header

import pipes

cmd = ' '.join(pipes.quote(a)
               for a in [ 'ls', 'hidden stdlib', '"already quoted"',
                          "with ' embedded", ])
print cmd

    


