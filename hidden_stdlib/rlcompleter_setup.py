#!/usr/bin/env python
# encoding: utf-8
"""Set up the rlcompleter library for tab completion at the interpreter prompt.
"""

import rlcompleter, readline
readline.parse_and_bind('tab: complete')
