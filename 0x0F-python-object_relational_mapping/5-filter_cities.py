#!/usr/bin/python3

'''
Write a script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
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
    cur.execute("SELECT cities.name FROM cities \
                WHERE cities.state_id = (\
                SELECT states.id FROM states WHERE states.name=%s) \
                ORDER BY cities.id ASC", (args[4],))
    rows = cur.fetchall()
    len = [len(rows), len(rows)]
    for row in rows:
        for item in row:
            if len[0] != 1 and len[1] != 1:
                print(f'{item}', end=', ')
            else:
                print(f'{item}')
            len[0] -= 1
