#!/usr/bin/env python
# encoding: utf-8
"""Load a custom object from JSON serlized version.
"""

import hmac
import json

def dict_to_object(d):    
    if '__class__' not in d: 
        return d
        
    class_name = d.pop('__class__')
    module_name = d.pop('__module__')
    signature = d.pop('__signature__')

    digest_maker = hmac.new('PyCon2011', 
                            module_name + class_name)
    expected_signature = digest_maker.hexdigest()
    if signature != expected_signature:
        raise ValueError('Invalid signature')
    
    print 'Loading "%s" from "%s"' % \
        (class_name, module_name)
    module = __import__(module_name)
    class_ = getattr(module, class_name)
    
    args = dict( (key.encode('ascii'), value)
                 for key, value in d.items())
    print 'Instantiating with', args
    
    inst = class_(**args)
    return inst

for encoded_object in [
    '''
    [{"s": "instance value goes here",
      "__signature__": "426f662f9fe3b3533d9ce7f9dcf8af77",
      "__module__": "json_myobj", "__class__": "MyObj"}]
    ''',
    
    # careful!
    '''
    [{"path": "/etc/passwd",
      "__signature__": "426f662f9fe3b3533d9ce7f9dcf8af77",
      "__module__": "os", "__class__": "unlink"}]
    ''',
    ]:
    try:
        myobj_instance = json.loads(
            encoded_object, 
            object_hook=dict_to_object,
            )
        print myobj_instance
    except Exception as err:
        print 'ERROR:', err
    print
