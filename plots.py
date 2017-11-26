import numpy as np
import matplotlib.pyplot as plt
import psycopg2
import psycopg2.extras
import stonog


duuupa = stonog.StonogDB()

conn_string = "dbname='stonoga' user='postgres' password=''"
print "Connecting to database\n -> %s " %(conn_string)

global conn
conn = psycopg2.connect(conn_string)

#setting variable to global
global cursor
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

work_mem = 2048

cursor.execute('SET work_mem TO %s', (work_mem,))
cursor.execute('SHOW work_mem')

memory = cursor.fetchone()
print 'Value: ',memory[0]
print 'Row:     ', memory

values_list = []
select_views = "SELECT views FROM views WHERE name = (%s)", "Zbigniew Stonoga - Scatman REMIX - YouTube"
cursor.executemany(select_views,values_list)
values_list = cursor.fetchall()
print (values_list)
