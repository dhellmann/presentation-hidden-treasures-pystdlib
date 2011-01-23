#!/bin/sh

sqlite3 -noheader test.db 'select * from users'
