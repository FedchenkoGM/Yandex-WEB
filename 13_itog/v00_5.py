import sqlite3
from flask import Flask


app = Flask(__name__)


@app.route('/experiments')
def experiments():
    with open('particles.txt') as f:
        bd = f.readline().strip()
        m = int(f.readline())

    connect = sqlite3.connect(bd)
    cur = connect.cursor()
    result = cur.execute("""SELECT laboratory, mass, exceeding, time 
                            FROM experiments    
                            WHERE reliability >= ?                        
                            ORDER BY time, mass, exceeding""", (m,)).fetchall()
    connect.close()
    d = {}
    if result:
        for elem in result:
            if elem[0] not in d:
                d[elem[0]] = [[elem[1], elem[2], elem[3]]]
            else:
                d[elem[0]].append([elem[1], elem[2], elem[3]])
    return d


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')



