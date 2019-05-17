#coding:utf-8

import sqlite3

conn = sqlite3.connect('./db.sqlite3')
c = conn.cursor()

c.execute("select * from vendor_food")

print c.fetchall()
