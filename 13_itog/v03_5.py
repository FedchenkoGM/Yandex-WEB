import sqlite3
from flask import Flask


app = Flask(__name__)


@app.route('/level')
def level():
    with open('natives.txt') as f:
        bd = f.readline().strip()
        name = f.readline().strip()

    connect = sqlite3.connect(bd)
    cur = connect.cursor()
    result = cur.execute(f"""SELECT settlement, level, tools
                            FROM inhabitants     
                            WHERE place == "{name}"                         
                            ORDER BY level DESC, settlement DESC""").fetchall()
    connect.close()
    ans = []
    print(result)
    if result:
        for elem in result:
            d = {}
            d['settlement'] = elem[0]
            d['level'] = elem[1]
            d['tools'] = elem[2]
            ans.append(d)
    return ans


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')



