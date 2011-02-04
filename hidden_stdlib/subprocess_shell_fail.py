#!/usr/bin/env python
# encoding: utf-8
"""Cannot use shell mode with lists of args.
"""

import subprocess

p = subprocess.Popen(
        ['ls', 
         '/Users/dhellmann/PyCon/Hidden Treasures',
         ], 
        shell=True,
        stdout=subprocess.PIPE)
stdout, stderr = p.communicate()

print stdout