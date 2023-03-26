import sqlite3
from flask import Flask


app = Flask(__name__)


@app.route('/darkness')
def darkness():
    with open('carbon.txt') as f:
        bd = f.readline().strip()
        m = int(f.readline())

    connect = sqlite3.connect(bd)
    cur = connect.cursor()
    result = cur.execute("""SELECT star, temperature, mass, size
                            FROM stars     
                            WHERE stage == "C" and temperature <= ?                        
                            ORDER BY temperature, mass DESC""", (m,)).fetchall()
    connect.close()
    ans = []
    print(result)
    if result:
        for elem in result:
            d = {}
            d['star'] = elem[0]
            d['temperature'] = elem[1]
            d['mass'] = elem[2]
            d['size'] = elem[3]
            ans.append(d)
    return ans


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')



