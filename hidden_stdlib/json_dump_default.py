#!/usr/bin/env python
# encoding: utf-8
"""Serialize a custom object to JSON.
"""

import hmac
import json
import json_myobj

def convert_to_builtin_type(obj):
    """object->dictionary"""
    print 'convert_to_builtin_type(%r)' % obj
    class_name = obj.__class__.__name__
    module_name = obj.__module__
    digest_maker = hmac.new('PyCon2011', 
                            module_name + class_name)
    signature = digest_maker.hexdigest()
    d = { '__class__':class_name,
          '__module__':module_name,
          '__signature__':signature,
          }
    d.update(obj.__dict__)
    return d

obj = json_myobj.MyObj('instance value goes here')
print json.dumps(obj, default=convert_to_builtin_type)
