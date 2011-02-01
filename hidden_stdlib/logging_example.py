#!/usr/bin/env python
# encoding: utf-8
"""Sending log output to a file and the console at the same time.
"""

import logging
import logging.handlers
import sys

console_format = '%(message)s'
file_format = '%(asctime)s %(levelname)6s %(name)s %(message)s'

# Log verbosely
root_logger = logging.getLogger('')
root_logger.setLevel(logging.DEBUG)

# Set up console output to stderr
console = logging.StreamHandler(sys.stderr)
console.setFormatter(logging.Formatter(console_format))
console.setLevel(logging.INFO) # TODO: command line switch
root_logger.addHandler(console)

# Include debug messages when logging to a file
file_handler = logging.handlers.RotatingFileHandler(
    'logging_example.log', # use a full path
    )
file_handler.setFormatter(logging.Formatter(file_format))
file_handler.setLevel(logging.DEBUG)
root_logger.addHandler(file_handler)

# Tracebacks should only go to the file
traceback_log = logging.getLogger('tracebacks')
traceback_log.propagate = False
traceback_log.setLevel(logging.ERROR)
traceback_log.addHandler(file_handler)

# Let the app or its libraries log messages with different levels
log = logging.getLogger(__name__)
log.info('on the console and in the file')
log.debug('only in the file')

# Send exceptions to the separate logger
try:
    raise RuntimeError('failure message')
except Exception as err:
    log.error(err) # for console output
    traceback_log.exception(err)
