#!/usr/bin/python3

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
    cur.execute("SELECT cities.name FROM cities \
                WHERE cities.state_id = (\
                SELECT states.id FROM states WHERE states.name=%s) \
                ORDER BY cities.id ASC", (args[4],))
    rows = cur.fetchall()
    len = len(rows)
    for row in rows:
        for item in row:
            if len != 1:
                print(f'{item}', end=', ')
            else:
                print(f'{item}')
            len -= 1
