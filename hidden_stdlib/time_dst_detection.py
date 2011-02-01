#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2011 Doug Hellmann.  All rights reserved.
#
"""Detect whether a datetime value is within daylight savings time or not.
"""
#end_pymotw_header

import time
import datetime

for dt in [ datetime.datetime(2011, 2, 9, 9, 0),
            datetime.datetime(2011, 9, 30, 9, 0),
            ]:
    
    # Convert datetime -> struct_time
    time_t = time.struct_time(dt.timetuple())

    # Round-trip: struct_time -> seconds -> struct_time
    local_time_t = time.localtime(time.mktime(time_t))

    # The answer is in tm_isdst
    print dt, bool(local_time_t.tm_isdst)
