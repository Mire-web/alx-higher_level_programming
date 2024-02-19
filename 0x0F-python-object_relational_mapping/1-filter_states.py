#!/usr/bin/python3
"""
AUTHOR: MIRE-WEB
Desc: Print all states starting with N
Date: 17/02/2024
"""
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         port=3306,
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states\
                WHERE states.name LIKE 'N%'\
                OR states.name LIKE 'n%'\
                ORDER BY states.id ASC")
    for item in cur.fetchall():
        print(item)
    cur.close()
    db.close()
