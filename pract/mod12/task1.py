import sqlite3

old_conn = sqlite3.connect('netflix.sqlite')
old_cursor = old_conn.cursor()

new_conn = sqlite3.connect('task1.sqlite')
new_cursor = new_conn.cursor()

new_cursor.execute('CREATE TABLE IF NOT EXISTS актеры (id INTEGER PRIMARY KEY, имя TEXT)')
new_cursor.execute('CREATE TABLE IF NOT EXISTS фильмы (id INTEGER PRIMARY KEY, название TEXT)')
new_cursor.execute('CREATE TABLE IF NOT EXISTS актер_фильм (id INTEGER PRIMARY KEY, id_актера INTEGER, id_фильма INTEGER)')

old_cursor.execute('SELECT "cast" FROM netflix_titles')
cast = old_cursor.fetchall()
new_cursor.executemany('INSERT INTO актеры ( имя ) VALUES (?)', cast)

old_cursor.execute('SELECT "title" FROM netflix_titles')
title = old_cursor.fetchall()
new_cursor.executemany('INSERT INTO фильмы (название) VALUES (?)', title)



old_conn.close()
new_conn.close()
