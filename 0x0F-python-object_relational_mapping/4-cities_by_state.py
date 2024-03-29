#!/usr/bin/python3
'''
a script that lists all cities from the database hbtn_0e_4_usa
'''

import sys
import MySQLdb

if __name__ == '__main__':
    args = sys.argv
    db = MySQLdb.connect(
            host='localhost',
            user=args[1],
            passwd=args[2],
            db=args[3],
            port=3306
        )
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities \
                INNER JOIN states ON cities.state_id=states.id \
                ORDER BY cities.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
