#!/usr/bin/python3
"""
Author: Mire-web
Desc: Return list of cities in state filtered by user input
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
    query = "SELECT cities.name FROM cities\
             JOIN states ON cities.state_id = states.id\
             WHERE (\
             SELECT id FROM states\
             WHERE states.name = %s) = cities.state_id\
             ORDER BY cities.id ASC"
    cur.execute(query, (args[4],))
    cities = cur.fetchall()
    if len(cities) > 0:
        for idx, item in enumerate(cities):
            for city in item:
                if idx < len(cities) - 1:
                    print(city, end=', ')
                else:
                    print(city)
    else:
        print()
