#!/usr/bin/env python
# encoding: utf-8
"""Sending log output to a file and the console at the same time.
"""

import logging
import logging.handlers
import sys

root_logger = logging.getLogger('')
root_logger.setLevel(logging.DEBUG)

# Set up console output to stderr
console = logging.StreamHandler(sys.stderr)
console.setFormatter(logging.Formatter('%(message)s'))
console.setLevel(logging.INFO)
root_logger.addHandler(console)

# Include debug messages when logging to a file
file_handler = logging.handlers.RotatingFileHandler(
    'logging_example.log', # use a full path
    )
file_handler.setFormatter(
    logging.Formatter('%(asctime)s %(levelname)6s %(name)s %(message)s')
    )
file_handler.setLevel(logging.DEBUG)
root_logger.addHandler(file_handler)

# Let the app or its libraries log messages of different levels
log = logging.getLogger(__name__)
log.info('this message appears on the console and in the file')
log.debug('this message is only in the file')
