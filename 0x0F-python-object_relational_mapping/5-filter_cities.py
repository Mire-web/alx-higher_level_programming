#!/usr/bin/python3
"""
Lists all cities in a state
Author: Mire
"""
import sys
import MySQLdb as sql


def main(username, password, db_name, state_name):
    db = sql.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=db_name,
        port=3306
    )
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities \
WHERE cities.state_id = (SELECT states.id FROM states \
WHERE states.name = %(state_name)s)", {'state_name': state_name})
    items = cur.fetchall()
    count = 1
    for item in items:
        for one in item:
            if count == len(items):
                print(one, end="")
            else:
                print(one, end=", ")
                count += 1
    print()

    cur.close()
    db.close()


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
