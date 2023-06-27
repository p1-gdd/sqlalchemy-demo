#!/bin/env python3
import mariadb
conn_params = {"database": "mariadb-demo", "user": "mariadb-user",
               "password": "mariadb-pass", "host": "127.0.0.1", "port": 3306}
msg = []; table_name = 'movie'
connection = mariadb.connect(**conn_params)
cursor = connection.cursor()
cursor.execute(f'CREATE TABLE {table_name}(title VARCHAR(255), year INT, score FLOAT);')
try:
    cursor.execute(f'INSERT INTO {table_name} VALUES ("P1nder", 2023, 6.9),("Painsec", 2022, 7.1),("Pv1", 2021, 9.6);')
    connection.commit()
    cursor.execute(f'SELECT title, score FROM {table_name} WHERE year>YEAR(CURRENT_DATE() - INTERVAL 2 YEAR) ORDER BY score DESC;', buffered=False)
    for movie in cursor.fetchall():
        msg.append(f'{movie[0]!r} is a {movie[1]} scored recent movie')
except mariadb.ProgrammingError:
    msg.append(f'Table {table_name!r} has NOT been created in the MariaDB database {conn_params["database"]!r}')
print('\n'.join(msg))
cursor.close()
connection.close()
