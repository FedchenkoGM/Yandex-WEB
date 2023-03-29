import sqlite3
from flask import Flask


app = Flask(__name__)


@app.route('/boring')
def boring():
    with open('request.txt') as f:
        bd = f.readline().strip()
        star = f.readline().strip()

    connect = sqlite3.connect(bd)
    cur = connect.cursor()
    result = cur.execute(f"""SELECT planet, climate_type
                            FROM climate     
                            WHERE star == "{star}" """).fetchall()
    connect.close()
    ans = {}
    print(result)
    if result:
        for elem in result:
            if elem[0] not in ans:
                ans[elem[0]] = {elem[1]}
            else:
                ans[elem[0]].add(elem[1])
        for elem in ans:
            ans[elem] = sorted(ans[elem], key = lambda x: (len(x), x))
    return ans


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')



