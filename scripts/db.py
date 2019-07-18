#!/usr/bin/env python3
# coding:utf-8

import sqlite3

scripts = [
    "../sql/schema.sql",
    "../sql/data.sql"
]

cnx = sqlite3.connect("../data/db.sqlite3")

for s in scripts:
    print(s)
    with open(s, "r") as f:
        cnx.executescript(f.read())

cnx.commit()
cnx.close()
        
