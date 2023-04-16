#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == '__main__':
    args = sys.argv

    db = MySQLdb.connect(host='localhost', user=args[1], passwd=args[2], db=args[3],port=3306) 
    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY states.id ASC')
    rows = cur.fetchall()
    for row in rows:
        print(row)
