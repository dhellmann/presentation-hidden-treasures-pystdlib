#!/usr/bin/env python
# encoding: utf-8
"""Signing and verifying messages with hmac
"""

import hashlib
import hmac
from cStringIO import StringIO
import pickle

message = 'The message'
encoded_message = pickle.dumps(message)

digest_maker = hmac.new('shared-secret-value')
digest_maker.update(encoded_message)
signature = digest_maker.hexdigest()

print 'Outgoing signature:', signature

# Simulate sending the message
buffer = StringIO('%s\n%d\n%s' % (signature,
                                  len(encoded_message),
                                  encoded_message
                                  ))

# "Receive" the message
read_signature = buffer.readline().rstrip() 
message_len = int(buffer.readline())
read_message = buffer.read(message_len)

# Check the signature of the incoming data
digest_maker = hmac.new('shared-secret-value',
                        read_message)
computed_signature = digest_maker.hexdigest()
print 'Computed signature:', signature

if computed_signature == read_signature:
    print '\nValid message, processed'
    safe_message = pickle.loads(read_message)
    print 'Message:', safe_message
else:
    raise ValueError('Invalid message, discarded')