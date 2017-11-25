import stonog

#obiekt = stonog.Example('dupa')
#obiekt.rzopa()
DB_class = stonog.StonogDB()
MakePlot_class = stonog.MakePlot(list, list)

print ('Choose what you want to do:\n 1. Check if connection works\n 2. Connect and insert rows with info from yt\n' +
' 3. Make a plot')

user_input = raw_input('Your choice: ')

try:
    user_input = int(user_input)
except ValueError:
    print ('Choose a number')


if user_input == 1:
    DB_class.connect()
    print ('sraka')

elif user_input == 2:
    try:
        DB_class.connect()
    except:
        print('Couldn\'t connect. Check database name.')
    DB_class.insert_rows()

elif user_input == 3:
    print ('This function is not yet ready.')
else:
    list = []
    list2 = []
    MakePlot_class.create_list_of_titles(list)
    MakePlot_class.select_views(list, list2)
