import requests           
import psycopg2           
import json               

conn = psycopg2.connect(
    dbname="base",
    user="postgres",
    password="20062007",
    host="localhost",
    port="5432"
)
cur = conn.cursor() 
cur.execute("SELECT COALESCE(MAX(attempt), 0) FROM executer;")
attempt = cur.fetchone()[0] + 1
url = "https://mapi.itstep.org/v1/mystat/aqtobe/schedule/get-existing-schedule?date_filter=2025-07-01"
headers = {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXV0aC5pdHN0ZXAub3JnXC9hcGlcL2F1dGhcL2xvZ2luIiwiaWF0IjoxNzUxODI0MjcxLCJleHAiOjE3NTI0MjkwNzEsIm5iZiI6MTc1MTgyNDI3MSwianRpIjoiTFBaVzRtb3gxaml2d1FZTyIsInN1YiI6MTczMiwiaWQiOjE3MzIsImlkX3VzZXJfc3RvcmFnZSI6ODYxMTEyNywiZW1haWwiOiJUYXpoaW1iZXRvdmE4M0BtYWlsLnJ1IiwidXNlcm5hbWUiOiJVdGVtYl9hYTUwIiwibmFtZSI6Ilx1MDQxMFx1MDQzYVx1MDQ0MVx1MDQzYlx1MDQ0MyBcdTA0MjNcdTA0NDJcdTA0MzVcdTA0M2NcdTA0MzFcdTA0MzVcdTA0NDJcdTA0M2VcdTA0MzJcdTA0MzAiLCJicmFuY2hfaWQiOjM5OCwicHJvamVjdF9pZCI6NTAsImxhbmciOiIiLCJwcm9maWxlIjoic3R1ZGVudCIsIm1vZHVsZSI6Im15c3RhdCIsImJyYW5jaF9hbGlhcyI6ImFxdG9iZSJ9.oEMaXWUjcK_Qb55PldE5bOkfs3HI4EOKGdGMVz0iJjs"}
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


