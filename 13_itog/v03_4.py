import sqlite3
import csv

connect = sqlite3.connect(input())
atr, m = input(), input()
cur = connect.cursor()
result = cur.execute(f"""SELECT title, name, localities.area, type 
                        FROM localities INNER JOIN continents ON localities.continent_id = continents.id 
                        INNER JOIN zones ON localities.zone_id = zones.id   
                        WHERE {atr} <= ?                       
                        ORDER BY localities.area DESC,title DESC""", (m, )).fetchall()
connect.close()

h = ['no', 'locality', 'continent', 'area', 'zone']
with open('geography.csv', 'w', newline='', encoding="utf8") as f:
    writer = csv.DictWriter(f, fieldnames=h, delimiter='_')
    writer.writeheader()
    if result:
        for ind, elem in enumerate(result):
            el = {}
            el['no'] = ind + 1
            el['locality'] = elem[0]
            el['continent'] = elem[1]
            el['area'] = elem[2]
            el['zone'] = elem[3]
            writer.writerow(el)
