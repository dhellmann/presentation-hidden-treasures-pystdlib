#!/usr/bin/env python
# encoding: utf-8
"""Serialize a custom object to JSON.
"""

import json
import json_myobj

def convert_to_builtin_type(obj):
    """Convert objects to a dictionary of their representation.
    """
    print 'convert_to_builtin_type(%r)' % obj
    d = { '__class__':obj.__class__.__name__, 
          '__module__':obj.__module__,
          }
    d.update(obj.__dict__)
    return d

obj = json_myobj.MyObj('instance value goes here')
print json.dumps(obj, default=convert_to_builtin_type)
