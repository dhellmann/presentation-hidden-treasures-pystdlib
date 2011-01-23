#!/usr/bin/env python
# encoding: utf-8
"""Quoting command line argument parts to build shell commands.
"""

import subprocess

cmd = subprocess.list2cmdline([
        'ls', 'hidden stdlib', '"already quoted"',
        "with ' embedded", ])
print cmd
