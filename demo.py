from multiprocessing import connection
import psycopg2

connection = psycopg2.connect('dbname=example user=almmello')

cursor = connection.cursor()


cursor.execute("""
  CREATE TABLE table2 (
    id INTEGER PRIMARY KEY,
    completed BOOLEAN NOT NULL DEFAULT False
  );
""")

cursor.execute('INSERT INTO table2 (id, completed) VALUES (1, true);')
# commit, so it does the executions on the db and persists in the db
connection.commit()

cursor.close()
connection.close()