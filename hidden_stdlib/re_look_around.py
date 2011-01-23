#!/usr/bin/env python
# encoding: utf-8
"""Positve look-ahead and negative look-behind assertions
"""

import re

# An email address: username@domain.tld
address = re.compile(
    r'''
    # Limit the top-level domains
    (?=.*\.(?:com|org|edu)$)

    ^(
       [\w\d.+-]+   # Account name
     
       (?<!noreply) # Ignore "noreply"

       @[\w\d.+-]+  # Domain name
    )$
    ''',
    re.UNICODE | re.VERBOSE)

candidates = [
    'first.last@example.com',
    'user@example.org',
    'ignored@example.co.uk',
    'noreply@example.com',
    ]

for candidate in candidates:
    print '{:25}'.format(candidate),
    match = address.search(candidate)
    if match:
        print 'MATCH     ', match.groups()
    else:
        print 'NO MATCH'
