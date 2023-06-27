#!/bin/env python3
import sqlite3
msg = []; db_file = 'sqlite.db'; table_name = 'movie'
connection = sqlite3.connect(db_file)
cursor = connection.cursor()
cursor.execute(f'CREATE TABLE {table_name}(title primary key, year integer, score real);')
cursor.execute('SELECT name FROM sqlite_master;')
if 'movie' not in cursor.fetchone():
    msg.append(f'Table {table_name!r} has NOT been created in the SQLite database {db_file!r}')
else:
    cursor.execute(f'INSERT INTO {table_name} VALUES ("P1nder", 2023, 6.9),("Painsec", 2022, 7.1),("Pv1", 2021, 9.6);')
    connection.commit()
    cursor.execute(f'SELECT title, score FROM {table_name} WHERE year>strftime("%Y", "now","start of year","-2 year") ORDER BY score DESC;')
    for movie in cursor.fetchall():
        msg.append(f'{movie[0]!r} is a {movie[1]} scored recent movie')
print('\n'.join(msg))
cursor.close()
connection.close()
