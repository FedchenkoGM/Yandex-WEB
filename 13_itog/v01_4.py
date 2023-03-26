import sqlite3
from pprint import pprint


with open('data.txt') as f:
    filename = f.readline().strip()
    year = int(f.readline())
connect = sqlite3.connect(filename)

cur = connect.cursor()
result = cur.execute(f"""SELECT id, name, load, crew, year 
                        FROM spaceships   
                        WHERE year = ?                       
                        ORDER BY load, name""", (year, )).fetchall()
connect.close()

ans = []
if result:
    for elem in result:
        el = {}
        el['id'] = elem[0]
        el['name'] = elem[1]
        el['load'] = elem[2]
        el['crew'] = elem[3]
        el['year'] = elem[4]
        ans.append(el)
    pprint(ans, sort_dicts=False)

