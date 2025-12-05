import requests           
import psycopg2           
import json               

conn = psycopg2.connect(
    dbname="base",
    user="postgres",
    password="",
    host="localhost",
    port="5432"
)
cur = conn.cursor() 
cur.execute("SELECT COALESCE(MAX(attempt), 0) FROM executer;")
attempt = cur.fetchone()[0] + 1
url = "https://mapi.itstep.org/v1/mystat/aqtobe/schedule/get-existing-schedule?date_filter=2025-07-01"
headers = {"Authorization": " "}
response = requests.get(url, headers=headers)   
data = response.json()               

cur.execute(
    "INSERT INTO executer (attempt, data) VALUES (%s, %s);",
    (attempt, json.dumps(data))
)

conn.commit()
cur.close()
conn.close()

print("Сохронено попытка:", attempt)



