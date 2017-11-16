from bs4 import BeautifulSoup
import urllib
import psycopg2
import psycopg2.extras


#try to connect
def main():
    conn_string = "dbname='stonoga' user='postgres' password=''"

    print "Connecting to database\n -> %s " %(conn_string)
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    work_mem = 2048

    cursor.execute('SET work_mem TO %s', (work_mem,))
    cursor.execute('SHOW work_mem')

    memory = cursor.fetchone()
    print 'Value: ',memory[0]
    print 'Row:     ', memory

    links = open('linki_stonoga.txt','r')
    id = 1
    for line in links:

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
        query = "INSERT INTO views VALUES (%s,%s,%s);"
        data = (id, title, int_count)
        id += 1
        cursor.execute (query,data)
        conn.commit()
        #cursor.execute ("""INSERT INTO views VALUES (%s,%s,%s);""",(DEFAULT, title, int_count))

if __name__ == "__main__":
    main()
