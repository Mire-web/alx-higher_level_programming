#!/usr/bin/python3
"""
Lists all states in the sql database
Author: Mire
"""


import MySQLdb as sql
import sys


def main(username, password, database):
    """
    Entry Point function
    username: user acct name
    password: user acct password
    database: database name
    """
    db = sql.connect(host="localhost", user=username,
                     passwd=password, db=database, port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC;")
    items = cur.fetchall()
    for item in items:
        print(item)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
