import mysql.connector

with open('config.txt', encoding='utf-8') as f:
    PASSWORD = f.read()
con = mysql.connector.connect(host='127.0.0.1', port=3306, database='kuruch', user='root', password=PASSWORD)
cur = con.cursor(dictionary=False)

for line in open("/db/kuruch.sql"):
    cur.execute(line)