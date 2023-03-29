import sqlite3
import csv

connect = sqlite3.connect(input())
table, atr  = input().split()
val = input()
cur = connect.cursor()
result = cur.execute(f"""SELECT stars.id, designation, name, distance, title, first 
                        FROM constellations INNER JOIN stars ON stars.const_id = constellations.id 
                        INNER JOIN elements ON stars.id_first = elements.id   
                        WHERE {table}.{atr} >= {val}                       
                        ORDER BY distance, designation""").fetchall()
connect.close()

h = ['id', 'star', 'constellation', 'distance', 'first', 'percent_first']
with open('main.csv', 'w', newline='', encoding="utf8") as f:
    writer = csv.DictWriter(f, fieldnames=h, delimiter=':')
    writer.writeheader()
    if result:
        for elem in result:
            el = {}
            el['id'] = elem[0]
            el['star'] = elem[1]
            el['constellation'] = elem[2]
            el['distance'] = elem[3]
            el['first'] = elem[4]
            el['percent_first'] = elem[5]
            writer.writerow(el)
