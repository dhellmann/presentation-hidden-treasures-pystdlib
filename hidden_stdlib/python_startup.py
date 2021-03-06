#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""Startup script to enable history saving and tab completion.

Adapted from http://docs.python.org/tutorial/interactive.html
"""
import os
import readline
import rlcompleter

# Tab completion
readline.parse_and_bind('tab: complete')

# Location of history file
if os.environ.get('VIRTUAL_ENV'):
    history_filename = os.path.expandvars("$VIRTUAL_ENV/.pyhistory")
else:
    history_filename = os.path.expanduser("~/.pyhistory")

# Load history on startup
if os.path.exists(history_filename):
    print 'Loading history from %s' % history_filename
    readline.read_history_file(history_filename)

# Use this to save the history:
# readline.write_history_file(history_filename)

# Clean up names
del os, rlcompleter, save_history, history_filename
