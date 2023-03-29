import sqlite3
from flask import Flask


app = Flask(__name__)


@app.route('/messages')
def messages():
    with open('news.txt') as f:
        bd = f.readline().strip()
        name = f.readline().strip()

    connect = sqlite3.connect(bd)
    cur = connect.cursor()
    result = cur.execute(f"""SELECT star, importance, duration
                            FROM messages     
                            WHERE constellation == "{name}"                         
                            ORDER BY importance DESC, duration""").fetchall()
    connect.close()
    ans = {}
    print(result)
    if result:
        for elem in result:
            if elem[0] not in ans:
                ans[elem[0]] = [[elem[1], elem[2]]]
            else:
                ans[elem[0]].append([elem[1], elem[2]])
    return ans


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')



