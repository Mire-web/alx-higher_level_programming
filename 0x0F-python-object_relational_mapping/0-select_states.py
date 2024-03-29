#!/usr/bin/python3
"""
AUTHOR: Mire-web
Desc: Prints all states from hbtn_0e_0_usa
Date: 17/02/2024
"""
import sys
import MySQLdb

if __name__ == '__main__':
    args = sys.argv
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=args[1],
                         passwd=args[2],
                         db=args[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    for item in cur.fetchall():
        print(item)
