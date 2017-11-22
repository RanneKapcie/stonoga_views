import numpy as np
import matplotlib.pyplot as plt
import psycopg2
import psycopg2.extras
import stonog


class MakePlot():

    Ston_class = stonog.StonogDB()

    def __init__(self,list_of_titles):
        self.list_of_titles = list_of_titles

    def create_list_of_titles(self):

        id = 1
        boolean = True

        #adding every title name to the list
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

    def select_views(self):

        self.create_list_of_titles()

        for title in list_of_titles:
            views_query = "SELECT views FROM views WHERE name = (%s)" % (title)
            cursor.execute(views_query)
            views = cursor.fetchall()
            print (views)

    if __name__ == "__main__":
        select_views()
