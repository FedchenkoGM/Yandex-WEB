import sqlite3
import csv

connect = sqlite3.connect(input())
atr, val = input().split()
table = input()
cur = connect.cursor()
result = cur.execute(f"""SELECT name, post, title, skill 
                        FROM crew INNER JOIN positions ON crew.post_id = positions.id 
                        INNER JOIN groups ON crew.group_id = groups.id   
                        WHERE {table}.{atr} >= ?                       
                        ORDER BY skill, name""", (val, )).fetchall()
connect.close()

h = ['no', 'name', 'post', 'group', 'skill']
with open('ship_law.csv', 'w', newline='', encoding="utf8") as f:
    writer = csv.DictWriter(f, fieldnames=h, delimiter=':')
    writer.writeheader()
    if result:
        for ind, elem in enumerate(result):
            el = {}
            el['no'] = ind + 1
            el['name'] = elem[0]
            el['post'] = elem[1]
            el['group'] = elem[2]
            el['skill'] = elem[3]
            writer.writerow(el)
