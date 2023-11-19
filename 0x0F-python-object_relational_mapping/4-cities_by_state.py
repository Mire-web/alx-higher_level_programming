#!/usr/bin/python3
"""
Lists all cities from database
Author: Mire
"""
import sys
import MySQLdb as sql


def main(username, password, database):
    db = sql.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=database,
        port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
FROM cities JOIN states ON states.id=cities.state_id \
ORDER BY cities.id ASC")
    items = cur.fetchall()
    for item in items:
        print(item)

    cur.close()
    db.close()


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
