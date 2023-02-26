from data.db_session import global_init, create_session
from data.users import User
from data.jobs import Jobs


def main():
    global_init(input())
    session = create_session()

    for job in session.query(Jobs).filter(Jobs.work_size < 20, Jobs.is_finished == False):
        print(f"{job}")


if __name__ == '__main__':
    main()





