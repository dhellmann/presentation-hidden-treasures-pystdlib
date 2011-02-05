#!/usr/bin/env python
# encoding: utf-8
"""Defining a custom type.
"""

import sqlite3
import pickle

class MyObj(object):
    def __init__(self, arg):
        self.arg = arg
    def __str__(self):
        return 'MyObj(%r)' % self.arg

# Register the functions for manipulating the type.

def adapter_func(obj):
    """memory -> storage"""
    print 'Saving:', obj
    return pickle.dumps(obj)

sqlite3.register_adapter(MyObj, adapter_func)

def converter_func(data):
    """storage -> memory"""
    return pickle.loads(data)
    
sqlite3.register_converter("MyObj", converter_func)

with sqlite3.connect(
        'type_demo.db',
        detect_types=sqlite3.PARSE_DECLTYPES) as conn:
    # Create a table with column of type "MyObj"
    conn.execute("""
    create table if not exists obj (
        id    integer primary key autoincrement not null,
        data  MyObj
    )
    """)
    cursor = conn.cursor()

    # Insert the objects into the database
    print 'Inserting:'
    to_save = [ (MyObj('this is a value to save'),),
                (MyObj(42),),
                ]
    cursor.executemany(
        "insert into obj (data) values (?)", 
        to_save)

    # Query the database for the objects just saved
    print '\nQuerying:'
    cursor.execute("select id, data from obj")
    for obj_id, obj in cursor.fetchall():
        print 'Retrieved', obj_id, type(obj), obj