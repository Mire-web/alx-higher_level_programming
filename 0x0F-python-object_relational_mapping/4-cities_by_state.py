#!/usr/bin/python3
"""
Author: Mire-web
Desc: List all cities from database
Date: 18/02/2024
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
    query = "SELECT cities.id, cities.name, states.name FROM cities\
             JOIN states ON cities.state_id\
             WHERE states.id = state_id\
             ORDER BY cities.id ASC"
    cur.execute(query)
    for item in cur.fetchall():
        print(item)
