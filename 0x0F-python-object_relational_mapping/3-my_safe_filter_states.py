#!/usr/bin/python3
"""
AUTHor: Mire-web
Desc: Return states that match user input while preventing sql injection
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
    query = "SELECT * FROM states WHERE states.name = %s"
    cur.execute(query, (args[4],))
    for item in cur.fetchall():
        print(item)
    cur.close()
    db.close()
