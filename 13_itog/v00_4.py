import sqlite3
import csv

connect = sqlite3.connect(input())
atr, table = input().split()
a1, a2 = map(int, input().split())
cur = connect.cursor()
result = cur.execute(f"""SELECT ships.designation, engines.designation, fuel_type, range 
                        FROM ships INNER JOIN engines ON ships.engine_id = engines.id 
                        INNER JOIN fuel ON engines.fuel_id = fuel.id   
                        WHERE {table}.{atr} BETWEEN ? AND ?                        
                        ORDER BY range DESC, ships.designation""", (a1, a2)).fetchall()
connect.close()

h = ['no', 'ship', 'engine_type', 'fuel_type', 'range']
with open('space_ship.csv', 'w', newline='', encoding="utf8") as f:
    writer = csv.DictWriter(f, fieldnames=h, delimiter=',')
    writer.writeheader()
    if result:
        for ind, elem in enumerate(result):
            el = {}
            el['no'] = ind + 1
            el['ship'] = elem[0]
            el['engine_type'] = elem[1]
            el['fuel_type'] = elem[2]
            el['range'] = elem[3]
            writer.writerow(el)