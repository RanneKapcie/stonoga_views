import stonog

DB_class = stonog.StonogDB()
MakePlot_class = stonog.MakePlot(list, list, list)
list1 = []
list2 = []
list3 = []

print ('Choose what you want to do:\n 1. Check if connection works\n 2. Connect and insert rows with info from yt\n' +
' 3. Make a plot')

user_input = raw_input('Your choice: ')

try:
    user_input = int(user_input)
except ValueError:
    print ('Choose a number')


if user_input == 1:
    DB_class.connect()

elif user_input == 2:
    try:
        DB_class.connect()
    except:
        print('Couldn\'t connect. Check database name.')
    DB_class.insert_rows()

elif user_input == 3:
    list_of_titles = MakePlot_class.create_list_of_titles(list1)
    MakePlot_class.create_plot(list_of_titles, list2, list3)

else:
    print 'No function'
