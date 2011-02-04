#!/usr/bin/env python
# encoding: utf-8
"""Proper shell-mode use of subprocess
"""

import subprocess
import pipes

args = [ 'ls', 
         '/Users/dhellmann/PyCon/Hidden Treasures']
cmd = ' '.join(pipes.quote(a) for a in args)
print 'RUNNING:', cmd

p = subprocess.Popen(cmd, 
                     shell=True,
                     stdout=subprocess.PIPE)
stdout, stderr = p.communicate()

print stdout