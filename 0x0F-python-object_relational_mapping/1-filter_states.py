#!/usr/bin/python
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         port=3306,
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states
                WHERE states.name LIKE 'N%'
                ORDER BY states.id ASC")
    for item in cur.fetchall():
        print(item)
