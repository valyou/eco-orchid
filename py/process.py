#/usr/bin/python2.7

import sys
import psycopg2
import psycopg2.extras

try:
    conn1 = psycopg2.connect("dbname=gh-2015_eco user=gh-2015_eco password=S3cret")
    conn2 = psycopg2.connect("dbname=gh-2015_eco user=gh-2015_eco password=S3cret")
except Exception as e:
    print "Unable to connect to the database: ", e

try:
    cur1 = conn1.cursor()
    cur1.execute("""SELECT * FROM sa2_cutdown""")
    rows = cur1.fetchall()
except Exception as e:
    print "Error when retrieving data: ", e

try:
    orig_stdout = sys.stdout
    f = file('../sql/4.sql', 'w')
    sys.stdout = f

    cur2 = conn2.cursor()
    for row in rows:
        statement = """SELECT COUNT(*) FROM orchid o, sa2_cutdown s WHERE gid = {0} AND ST_Within(o.geom, s.geom)""".format(row[0])
        cur2.execute(statement)
        res = cur2.fetchone()
        print "INSERT INTO \"public\".\"eco_value\" (\"sa2_main_11\", \"name\", \"code\", \"value_raw\") VALUES ('{0}', 'orchid', 'ecology', {1});".format(row[2], res[0])

    sys.stdout = orig_stdout
    f.close()
except Exception as e:
    print "error", e

conn2.close()
conn1.close()