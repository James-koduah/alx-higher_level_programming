#!/usr/bin/python3
'''
List names of 'N' in Table states from database hbtn_0e_0_usa
Usage: ./0-select_states.py <username> <password> <database>
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
    cur.execute("SELECT * FROM states WHERE states.name like BINARY 'N%'"
                "ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
