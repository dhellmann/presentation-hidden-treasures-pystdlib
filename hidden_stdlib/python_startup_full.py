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

# Save history on interpreter exit
import atexit
def save_history(history_filename=history_filename):
    print 'Saving history to %s' % history_filename
    import readline
    readline.write_history_file(history_filename)
atexit.register(save_history)

# Clean up names
del os, readline, rlcompleter, save_history, history_filename, atexit
