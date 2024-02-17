#!/usr/bin/python
"""
AUTHor: MIre-web
Desc: Return states that match user input
Date: 17/02/2024
"""
import MySQLdb
import sys


args = sys.argv
if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost',
                         user=args[1],
                         port=3306,
                         passwd=args[2],
                         db=args[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states\
                WHERE name = \'{}\'\
                ORDER BY id ASC".format(args[4]))
    for item in cur.fetchall():
        print(item)
