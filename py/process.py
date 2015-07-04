#/usr/bin/python2.7

import sys
import math
import psycopg2
import psycopg2.extras

def get_value(raw_value):
    if raw_value == 0:
        return 0
    elif raw_value > 250:
        return 10
    else:
        return int(math.ceil((float(raw_value) / float(250)) * 10))

def get_description(value):
    if value == 0:
        return "No Orchid sighting in the area"
    elif value == 1:
        return "1 Orchid sighting in the area"
    else:
        return "{0} Orchid sightings in the area".format(value)


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
        filterSql = """SELECT COUNT(*) FROM orchid o, sa2_cutdown s WHERE gid = {0} AND ST_Within(o.geom, s.geom)""".format(row[0])
        cur2.execute(filterSql)
        result = cur2.fetchone()

        raw_value = result[0]
        value = get_value(raw_value)
        description = get_description(raw_value)
        insertSql = "INSERT INTO \"public\".\"category_values\" (\"gid\", \"category_code\", \"raw_value\", \"value\", \"description\") VALUES ('{0}', 'ORCHID', {1}, {2}, '{3}');".format(row[1], raw_value, value, description)
        print insertSql

    sys.stdout = orig_stdout
    f.close()
except Exception as e:
    print "error", e

conn2.close()
conn1.close()