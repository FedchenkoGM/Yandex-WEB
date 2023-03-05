from flask import Flask, render_template
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def index():
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    users = session.query(User).all()
    names = {name.id: (name.surname, name.name) for name in users}
    print(jobs)
    print(users)
    print(names)
    print(len(names), len(jobs))
    print(users[0], type(users[0]))
    return render_template("index.html", jobs=jobs, names=names)


def main():
    db_session.global_init("db/mars_explorer.sqlite")
    app.run()


if __name__ == '__main__':
    main()
