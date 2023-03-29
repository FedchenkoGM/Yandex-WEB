import sqlite3
from flask import Flask


app = Flask(__name__)


@app.route('/path')
def path():
    with open('star_track.txt') as f:
        bd = f.readline().strip()
        name = f.readline().strip()

    connect = sqlite3.connect(bd)
    cur = connect.cursor()
    result = cur.execute(f"""SELECT star, mass, time
                            FROM supernova     
                            WHERE sleeve == "{name}"                         
                            ORDER BY time DESC, star""").fetchall()
    connect.close()
    ans = []
    print(result)
    if result:
        for elem in result:
            d = {}
            d['star'] = elem[0]
            d['mass'] = elem[1]
            d['duration'] = elem[2]
            ans.append(d)
    return ans


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')



