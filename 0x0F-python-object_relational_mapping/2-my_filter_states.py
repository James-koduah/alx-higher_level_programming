#!/usr/bin/python3
'''
    a script that takes in an argument and displays all values
    in the states table of hbtn_0e_0_usa where name matches the argument.

    Your script should take 4 arguments:
    mysql username, mysql password, database name and state name searched
    (no argument validation needed)
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
    cur.execute("SELECT * FROM states \
                WHERE name = '{}' \
                ORDER BY states.id ASC".format(args[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
