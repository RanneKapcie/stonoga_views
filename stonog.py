from bs4 import BeautifulSoup
import urllib
import psycopg2
import psycopg2.extras
import numpy as np
import matplotlib.pyplot as plt
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

    def __init__(self, list_of_titles, list_of_views, list_of_timestamps):

        self.list_of_titles = list_of_titles
        self.list_of_views = list_of_views
        self.list_of_timestamps = list_of_timestamps

    #queries the database and returns a list of titles in a database
    def create_list_of_titles(self, list_of_titles):

        StonogDB_class = StonogDB()
        StonogDB_class.connect()

        id_query = "SELECT id FROM views2 ORDER BY id LIMIT 1;"
        cursor.execute(id_query)
        id = cursor.fetchall()
        id = id[0][0]

        boolean = True

        #adding every title name to the list

        title_query = "SELECT title FROM views2"
        cursor.execute(title_query)
        title = cursor.fetchall()
        list_of_titles = set(map(tuple, title))
        list_of_titles = map(list, set(list_of_titles))
        return list_of_titles

    def select_views(self, list_of_titles, list_of_views, list_of_timestamps):

        list_of_titles = self.create_list_of_titles(list_of_titles)

        i = 0
        for title in list_of_titles:
            title = str(title[0])

            #fetching numbers of views from every title that is in list_of_titles
            select_views = "SELECT views_num, time FROM views2 WHERE title = (%s); "
            cursor.execute(select_views,(title,))
            views = cursor.fetchall()

            for view in views:
                list_of_views.append(view[0])
                list_of_timestamps.append(view[1])
            i += 1
        print list_of_titles
    def create_plot(self, list_of_titles, list_of_views, list_of_timestamps):

        self.select_views(list_of_titles, list_of_views, list_of_timestamps)
        #print list_of_views
        print list_of_titles
        #print out all titles with numbers
        id = 1
        for title in list_of_titles:
            print id, title
            id += 1

        #user has to choose which title to plot (by numbers printed before)
        user_choice = raw_input('Choose which video stats you want on a plot: ')
        user_choice = int(user_choice) - 1

        #setting values which are used to slice only views from chosen video
        slice_start = user_choice * (len(list_of_views)/len(list_of_titles))
        slice_end = (user_choice + 1) * ((len(list_of_views)/len(list_of_titles)))
        #slicing lists
        list_of_views = list_of_views[slice_start:slice_end]
        list_of_timestamps = list_of_timestamps[slice_start:slice_end]
        #convert lists to numpy arrays
        list_of_timestamps = np.array(list_of_timestamps)
        list_of_views = np.array(list_of_views)

        #creating a plot
        plt.plot(list_of_timestamps,list_of_views)
        plt.ylabel('Number of views')
        plt.xlabel('Date')
        plt.title(list_of_titles[user_choice][0], loc = 'right')
        plt.show()
