#!/usr/bin/env python
# encoding: utf-8
"""Show the garbage collector status on program exit.
"""

import atexit
import tempfile
import shutil

class TempDirFactory(object):
    def __init__(self):
        self.created = []
    def mkdir(self):
        new_dir_name = tempfile.mkdtemp()
        self.created.append(new_dir_name)
        return new_dir_name
    def cleanup(self):
        for dirname in self.created:
            print 'Removing', dirname
            shutil.rmtree(dirname, ignore_errors=True)

factory = TempDirFactory()
atexit.register(factory.cleanup)

dirname = factory.mkdir()
print 'Working with', dirname
