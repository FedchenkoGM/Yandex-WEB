import sqlite3
import csv

connect = sqlite3.connect(input())
table, atr, m = input(), input(), input()
cur = connect.cursor()
result = cur.execute(f"""SELECT planet, title, type, acceleration 
                        FROM planets INNER JOIN stars ON planets.star_id = stars.id 
                        INNER JOIN life ON planets.life_id = life.id   
                        WHERE {table}.{atr} >= ?                       
                        ORDER BY title, acceleration""", (m, )).fetchall()
connect.close()

h = ['no', 'planet', 'star', 'mode', 'acceleration']
with open('suitable.csv', 'w', newline='', encoding="utf8") as f:
    writer = csv.DictWriter(f, fieldnames=h, delimiter=';')
    writer.writeheader()
    if result:
        for ind, elem in enumerate(result):
            el = {}
            el['no'] = ind + 1
            el['planet'] = elem[0]
            el['star'] = elem[1]
            el['mode'] = elem[2]
            el['acceleration'] = elem[3]
            writer.writerow(el)
