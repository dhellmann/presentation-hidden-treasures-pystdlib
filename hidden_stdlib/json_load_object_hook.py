#!/usr/bin/env python
# encoding: utf-8
"""Load a custom object from JSON serlized version.
"""

import json

def dict_to_object(d):
    """Convert dictionaries containing object properties to custom objects.
    """
    if '__class__' in d:
        class_name = d.pop('__class__')
        module_name = d.pop('__module__')
        print 'Loading "%s" from "%s"' % (class_name, module_name)
        module = __import__(module_name)
        class_ = getattr(module, class_name)
        args = dict( (key.encode('ascii'), value)
                     for key, value in d.items())
        print 'Instantiating with', args
        inst = class_(**args)
    else:
        inst = d
    return inst

encoded_object = '''
    [{"s": "instance value goes here",
      "__module__": "json_myobj", "__class__": "MyObj"}]
    '''

myobj_instance = json.loads(encoded_object,
                            object_hook=dict_to_object)
print myobj_instance
