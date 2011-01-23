#!/bin/sh

rm -f test.db

sqlite3 test.db <<EOF

CREATE TABLE users (
  fullname text,
  username text,
  email    text
);

INSERT INTO users (fullname, username, email) 
VALUES ('Doug Hellmann', 'dhellmann', 'doug.hellmann@gmail.com');

INSERT INTO users (fullname, username, email) 
VALUES ('Guest account, no login', 'guest', 'guest@example.com');

EOF
