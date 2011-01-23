#!/usr/bin/env python
# encoding: utf-8
"""Signing and verifying messages with hmac
"""

import hmac
from cStringIO import StringIO

message = 'The message'

digest_maker = hmac.new('shared-secret-value')
digest_maker.update(message)
signature = digest_maker.hexdigest()

# Simulate sending a corrupted version of the message
buffer = StringIO('%s\n%d\n%s' % (signature,
                                  len(message),
                                  message[::-1],
                                  ))

# "Receive" the message
read_signature = buffer.readline().rstrip() 
message_len = int(buffer.readline())
read_message = buffer.read(message_len)

# Check the signature of the incoming data
digest_maker = hmac.new('shared-secret-value', read_message)
computed_signature = digest_maker.hexdigest()

if computed_signature == read_signature:
    print '  Valid message, processed'
else:
    print '  Invalid message, discarded'
    
