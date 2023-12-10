import sqlite3


conn_original = sqlite3.connect('netflix.sqlite')
cursor_original = conn_original.cursor()

conn_task1 = sqlite3.connect('task1.sqlite')
cursor_task1 = conn_task1.cursor()


cursor_task1.execute('''CREATE TABLE actors (
                        actor_id INTEGER PRIMARY KEY,
                        actor_name TEXT)''')

cursor_task1.execute('''CREATE TABLE movies (
                        movie_id INTEGER PRIMARY KEY,
                        movie_name TEXT)''')

cursor_task1.execute('''CREATE TABLE actor_movie (
                        actor_id INTEGER,
                        movie_id INTEGER,
                        FOREIGN KEY (actor_id) REFERENCES actors(actor_id),
                        FOREIGN KEY (movie_id) REFERENCES movies(movie_id))''')


cursor_original.execute('INSERT INTO actors SELECT DISTINCT cast FROM netflix')
cursor_original.execute('INSERT INTO movies SELECT DISTINCT title FROM netflix')

conn_original.close()
conn_task1.close()
