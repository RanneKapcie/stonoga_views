import numpy as np
import matplotlib.pyplot as plt
import psycopg2
import psycopg2.extras
import stonog


class MakePlot():

    list_of_titles = []

    def __init__(self,list_of_titles):
        self.list_of_titles = list_of_titles

    def connect():
        stonog.StonogDB.main()

    def create_list_of_titles():

        id = 1
        boolean = True
        while boolean == True:

            title_query = "SELECT name FROM views WHERE id = (%s)" % (id)
            cursor.execute(title_query)
            title = cursor.fetchall()
            title = title[0][0]

            if title in list_of_titles:
                boolean = False
            else:
                list_of_titles.append(title)
                id += 1

    def select_views():

        create_list_of_titles()

        for title in list_of_titles:
            views_query[] = "SELECT views FROM views WHERE name = (%s)" % (title)
            
