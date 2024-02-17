#!/usr/bin/python3
import MySQLdb
import sys
"""
    Module that performs MySQL query through MySQLdb module.
"""


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")

    cur = conn.cursor()

    stmt = "SELECT c.name, s.name FROM cities c INNER JOIN states s ON \
    c.state_id = s.id ORDER BY c.id"
    cur.execute(stmt)
    query_rows = cur.fetchall()

    i = 0
    for row in query_rows:
        if row[1] == sys.argv[4]:
            if i != 0:
                print(', ', end='')
            print(row[0], end='')
            i += 1
    print('')

    cur.close()
    conn.close()
