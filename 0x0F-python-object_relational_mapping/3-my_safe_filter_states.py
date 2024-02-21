#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    try:
        conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3], charset="utf8")

        cur = conn.cursor()
        stmt = "SELECT id, name FROM states WHERE name = %s ORDER BY id ASC"
        cur.execute(stmt, (sys.argv[4],))
        query_rows = cur.fetchall()

        for row in query_rows:
            print(row)

        cur.close()
        conn.close()
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
