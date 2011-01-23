#!/usr/bin/env python
# encoding: utf-8
"""Parse email addresses
"""

import email.utils

for addr in [ 'Doug Hellmann <doug.hellmann@gmail.com>',
              'doug.hellmann@gmail.com',
              ]:
    print '{:15} {}'.format(*email.utils.parseaddr(addr))
