import sqlite3
import csv

connect = sqlite3.connect(input())
table, atr  = input(), input()
val = input()
cur = connect.cursor()
result = cur.execute(f"""SELECT colonies.id, leader, planet, name, number, life_zone 
                        FROM colonies INNER JOIN planets ON colonies.planet_id = planets.id 
                        INNER JOIN stars ON planets.star_id = stars.id   
                        WHERE {table}.{atr} <= {val}                       
                        ORDER BY planet, leader""").fetchall()
connect.close()

h = ['colony_id', 'leader', 'planet_name', 'star_name', 'number', 'life_zone']
with open('response.csv', 'w', newline='', encoding="utf8") as f:
    writer = csv.DictWriter(f, fieldnames=h, delimiter=':')
    writer.writeheader()
    if result:
        for elem in result:
            el = {}
            el['colony_id'] = elem[0]
            el['leader'] = elem[1]
            el['planet_name'] = elem[2]
            el['star_name'] = elem[3]
            el['number'] = elem[4]
            el['life_zone'] = elem[5]
            writer.writerow(el)
