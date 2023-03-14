import psycopg2

connection = psycopg2.connect(
    database="demo",
    user='postgres',
    password='12345',
    host='localhost',
    port=5432
)

cur = connection.cursor()

cur.execute("select * from seats")
print(cur.fetchone())
