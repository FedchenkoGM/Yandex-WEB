import sqlite3
import csv

connect = sqlite3.connect(input())
atr = input()
table = atr.split('.')[0]
cur = connect.cursor()
result = cur.execute(f"""SELECT galaxies.sign, type, range, size, stars 
                        FROM galaxies INNER JOIN types ON galaxies.type_id = types.id 
                        INNER JOIN luminosities ON galaxies.luminosity_id = luminosities.id   
                        WHERE {atr} = (SELECT min({atr}) FROM {table})                       
                        ORDER BY size DESC, sign DESC""").fetchall()
connect.close()

h = ['no', 'galaxy', 'type', 'luminosity', 'size', 'stars']
with open('collisions.csv', 'w', newline='', encoding="utf8") as f:
    writer = csv.DictWriter(f, fieldnames=h, delimiter='#')
    writer.writeheader()
    if result:
        for ind, elem in enumerate(result):
            el = {}
            el['no'] = ind + 1
            el['galaxy'] = elem[0]
            el['type'] = elem[1]
            el['luminosity'] = elem[2]
            el['size'] = elem[3]
            el['stars'] = elem[4]
            writer.writerow(el)