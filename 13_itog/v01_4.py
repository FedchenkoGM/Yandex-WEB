import sqlite3
from flask import Flask


app = Flask(__name__)


@app.route('/schedule')
def schedule():
    with open('data.txt') as f:
        bd = f.readline().strip()
        year = int(f.readline())

    connect = sqlite3.connect(bd)
    cur = connect.cursor()
    result = cur.execute(f"""SELECT id, name, load, crew, year 
                            FROM spaceships   
                            WHERE year = ?                       
                            ORDER BY load, name""", (year,)).fetchall()
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
    return ans


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')
