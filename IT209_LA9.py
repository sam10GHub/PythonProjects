## Assignment: IT209 – LAB 9 (LA9)
# Purpose:Processing CSV Formatted Data
# Name: Samuel Essandoh



movies = [[1939, 'Gone With the Wind', 'drama'],
          [1943, 'Casablanca', 'drama'],
          [1954, 'On the Waterfront', 'drama'],
          [1957, 'The Bridge on the River Kwai', 'historical'],
          [1961, 'West Side Story', 'musical'],
          [1965, 'The Sound of Music', 'musical'],
          [1969, 'Midnight Cowboy', 'drama'],
          [1972, 'The Godfather', 'drama'],
          [1973, 'The Sting', 'comedy'],
          [1977, 'Annie Hall', 'comedy'],
          [1981, 'Chariots of Fire', 'drama'],
          [1982, 'Gandhi', 'historical'],
          [1984, 'Amadeus', 'historical'],
          [1986, 'Platoon', 'action'],
          [1988, 'Rain Man', 'drama'],
          [1990, 'Dances with Wolves', 'western'],
          [1991, 'The Silence of the Lambs', 'drama'],
          [1992, 'Unforgiven', 'western'],
          [1993, 'Schindler s List', 'historical'],
          [1994, 'Forrest Gump', 'comedy'],
          [1995, 'Braveheart', 'historical'],
          [1998, 'Shakespeare in Love', 'comedy'],
          [2001, 'A Beautiful Mind', 'historical'],
          [2002, 'Chicago', 'musical'],
          [2009, 'The Hurt Locker', 'action'],
          [2012, 'Argo', 'historical'],
          [2013, '12 Years a Slave', 'drama'],
          [2014, 'Birdman', 'comedy'],
          [2016, 'Moonlight', 'drama'],
          [2017, 'The Shape of Water', 'fantasy'],
          [2018, 'Green Book', 'drama'],
          [2019, 'Parasite', 'drama'],
          [2020, 'Nomadland', 'drama'],
          [2021, 'CODA', 'drama'],
          [2022, 'Everything Everywhere All at Once', 'comedy-drama'] ]


#1.  Write the list to a moviesLab9.txt in csv format
input('\n1. Hit "Enter" to write the movie list to a file in csv format' )
# ...code goes here...............
csv = open('moviesLab9.txt', 'w')
for data in movies:
    line ='{}, {}, {}\n'.format(data[0], data[1],data[2])
    csv.write(line)
csv.close()





# 2.  Inspect the file just created (no code)
print('\n\n\n2. Inspect the csv file just created using a text editor such as Notepad.')
print('Add three new movie records at the end of the file using EXCEL or Notepad: ')
print('1976, Rocky, drama')
print('1997, Titanic, historical')
print('2011, The Artist, comedy')
print('\nAfter adding, hit "Enter" to continue by reading the file into ')
print(' a nested list similar to the one given, the format: ')
print("[ [1939, 'Gone with the Wind', 'drama'], ")
print("  [1943, 'Casablanca', 'drama'], etc. ")
print('\nKeep the list in sorted order by year ')
input('\n\n"Enter" to continue')
#  ...no code is needed for this step, only manually reading and updating the file


# 3.  Read and print the csv file you just updated
input('\n\n3. "Enter" to read the updated csv format text file and create the movie list ')
#  ...code goes here................

movies_updated = []
with open('moviesLab9.txt', 'r') as f:
    for line in f:
        year, title, genre = line.strip().split(', ')
        movies_updated.append([int(year), title, genre])

print(movies_updated)



# 4.  prompt for a category and display all movie titles in that category
#     Continue prompting for a category until the user signals to quit.
input('\n\n4. "Enter" to begin prompting for a search category \n')
# ...code goes here.................
while True:
    category = input("Enter a movie category or 'q' to quit: ")
    if category == 'q':
        break
    else:
        for movie in movies_updated:
            if movie[2] == category:
                print(movie[1])


input('\n\nHit "Enter" to end program')
