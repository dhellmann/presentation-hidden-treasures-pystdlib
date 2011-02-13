#!/usr/bin/env python
# encoding: utf-8
"""Sending log output to a file and the console at the same time.
"""

import logging
import logging.handlers
import sys

# Log verbosely
root_logger = logging.getLogger('')
root_logger.setLevel(logging.DEBUG)

# Set up console output to stderr
console = logging.StreamHandler(sys.stderr)
console_format = '%(message)s'
console.setFormatter(logging.Formatter(console_format))
console.setLevel(logging.INFO) # TODO: command line switch
root_logger.addHandler(console)

# Include debug messages when logging to a file
file_handler = logging.handlers.RotatingFileHandler(
    'logging_example.log', # use a full path
    )
file_format = '%(asctime)s %(levelname)6s %(name)s %(message)s'
file_handler.setFormatter(logging.Formatter(file_format))
file_handler.setLevel(logging.DEBUG)
root_logger.addHandler(file_handler)

# Log sample messages with different levels
log = logging.getLogger(__name__)
log.info('on the console and in the file')
log.debug('only in the file')
log.error('simple error message')

# Replace excepthook with logger
def log_exception(exc_type, exc_value, traceback):
    logging.getLogger(__name__).error(exc_value)
sys.excepthook = log_exception

# Send exceptions to the logger automatically
raise RuntimeError('failure message')
