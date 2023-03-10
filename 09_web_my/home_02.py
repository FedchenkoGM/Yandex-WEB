from data.db_session import global_init, create_session
from data.users import User
from data.jobs import Jobs


def main():
    global_init(input())
    session = create_session()

    for user in session.query(User).filter((User.position.like('%chief%')) | (User.position.like('%middle%'))):
        print(f"{user} {user.position}")


if __name__ == '__main__':
    main()





