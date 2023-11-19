#!/usr/bin/python3
"""
Filter the database for states matching user input
Author: Mire
"""


import sys
import MySQLdb as sql


def main(username, password, database, name):
    db = sql.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=database,
        port=3306
    )
    cur = db.cursor()
    cur.execute(("SELECT * FROM states \
WHERE BINARY states.name = '{}' ORDER BY states.id").format(name))
    items = cur.fetchall()
    for item in items:
        print(item)

    cur.close()
    db.close()


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
