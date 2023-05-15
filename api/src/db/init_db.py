from db_utils import get_db_connection

connection = get_db_connection()

with open('schema.sql') as f:
    connection.executescript(f.read())

# cur = connection.cursor()

# cur.execute("INSERT INTO todos (title, completed) VALUES (?, ?)",
#             ('Learn Python', 1)
#             )

# cur.execute("INSERT INTO todos (title, completed) VALUES (?, ?)",
#             ('Finish InduLog Project', 0)
#             )

# connection.commit()
# connection.close()