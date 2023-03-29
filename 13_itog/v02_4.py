import sqlite3
import csv

connect = sqlite3.connect(input())
genres = input().split()
cur = connect.cursor()
result = cur.execute(f"""SELECT title, name, genre, duration 
                        FROM works INNER JOIN authors ON works.author_id = authors.id 
                        INNER JOIN genres ON works.genre_id = genres.id   
                        WHERE genre IN ("{'", "'.join(genres)}")                       
                        ORDER BY duration DESC,title""").fetchall()
connect.close()

h = ['no', 'title', 'author', 'genre', 'duration']
with open('silent.csv', 'w', newline='', encoding="utf8") as f:
    writer = csv.DictWriter(f, fieldnames=h, delimiter=',')
    writer.writeheader()
    if result:
        for ind, elem in enumerate(result):
            el = {}
            el['no'] = ind + 1
            el['title'] = elem[0]
            el['author'] = elem[1]
            el['genre'] = elem[2]
            el['duration'] = elem[3]
            writer.writerow(el)


