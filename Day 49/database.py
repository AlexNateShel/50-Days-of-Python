import sqlite3

con = sqlite3.connect('my_movies.db')
cur = con.cursor()

# Create a table in the database
try:
    cur.execute('CREATE TABLE movies_table(year, title, genre)')

except sqlite3.OperationalError:
    print('Table already exists')

# Create a variable of all the movies
movies = [(2009, 'Brothers', 'Drama'),
          (2002, 'Spider-Man', 'Sci-fi'),
          (2009, 'WathMen', 'Drama'),
          (2010, 'Inception', 'Sci-fi'),
          (2009, 'Avatar', 'Fantasy')]

cur.executemany('''INSERT INTO movies_table VALUES(?, ?, ?);
''', movies)

# Commit and close
con.commit()
con.close()

con = sqlite3.connect('my_movies.db')
cur = con.cursor()


# Select all from table
table = cur.execute('SELECT * FROM movies_table;')

# Find movies named 'Brothers'
for movie in table:
    print(movie)

row_brothers = cur.execute('SELECT *' 
                           'FROM movies_table' 
                           'WHERE title = "Brothers";')

# Find movies from 2009
for movie in row_brothers:
    print(movie)

    year_2009 = cur.execute('SELECT *'
                            'FROM movies_table' 
                            'WHERE year = 2009')

for year in year_2009:
    print(year)

# Find movies from genre Fantasy or Drama
for genre in cur.execute('SELECT *'
                         'FROM movies_table'
                         'WHERE genre = "Fantasy OR genre = "Drama";'):
        print(genre)

# Delete movies from table
cur.execute('DELETE FROM movies_table;')
con.commit()