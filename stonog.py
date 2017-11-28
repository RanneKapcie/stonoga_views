from bs4 import BeautifulSoup
import urllib
import psycopg2
import psycopg2.extras
from datetime import datetime

links = open('linki_stonoga.txt','r')

class Example:
    def __init__(self, dupa):
        self.dupa = dupa

    def rzopa(self):
        print (self.dupa)

class StonogDB:

    #try to connect
    def connect(self):
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

        #getting id of last record in the table

    def insert_rows(self):

        #id_query = "SELECT id FROM views ORDER BY id DESC LIMIT 1;"
        #cursor.execute(id_query)
        #id = cursor.fetchone()
        #id = id[0][0]

        for line in links:

            dt = datetime.now()
            #getting number of views
            url = line
            html = urllib.urlopen(url)
            soup = BeautifulSoup(html,'lxml')
            tag = soup.find(itemprop = 'interactionCount')
            int_count = tag.get('content')

            #finding title of video
            name = soup.find(name = 'title')
            title = soup.title.string
            print title,': ',int_count

            query = "INSERT INTO views2 (title,views_num,time) VALUES (%s,%s,%s);"

            data = (title, int_count, dt)
            cursor.execute (query,data)
            conn.commit()
            #cursor.execute ("""INSERT INTO views VALUES (%s,%s,%s);""",(DEFAULT, title, int_count))

class MakePlot():

    def __init__(self, list_of_titles, dict_titles_views):

        self.list_of_titles = list_of_titles
        self.dict_titles_views = dict_titles_views

    #queries the database and returns a list of titles in a database
    def create_list_of_titles(self, list_of_titles):

        self.list_of_titles = list_of_titles
        StonogDB_class = StonogDB()
        StonogDB_class.connect()

        id_query = "SELECT id FROM views2 ORDER BY id LIMIT 1;"
        cursor.execute(id_query)
        id = cursor.fetchall()
        id = id[0][0]

        boolean = True

        #adding every title name to the list
        while boolean == True:

            title_query = "SELECT title FROM views2 WHERE id = (%s)"
            cursor.execute(title_query, [id])
            title = cursor.fetchall()
            title = title[0][0]

            if title in list_of_titles:
                boolean = False
            else:
                list_of_titles.append(title)
                id += 1
        return list_of_titles

    def select_views(self, list_of_titles, list_titles_views):

        #creating list of lists
        list_of_views = list()

        i = 0
        for title in list_of_titles:

            title = str(title)

            #fetching numbers of views from every title that is in list_of_titles
            select_views = "SELECT views_num FROM views2 WHERE title = (%s); "
            cursor.execute(select_views,(title,))
            views = cursor.fetchall()
            for view in views:
                list_of_views.append(view)
            i += 1
        print list_of_views
