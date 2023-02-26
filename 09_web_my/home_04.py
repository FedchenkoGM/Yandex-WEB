from data.db_session import global_init, create_session
from data.users import User
from data.jobs import Jobs


def main():
    global_init(input())
    session = create_session()

    m = 0
    for job in session.query(Jobs):
        k = len(job.collaborators.split(', '))
        if k > m:
            ans = [job.team_leader]
            m = k
        elif k == m:
            ans += [job.team_leader]

    for id in set(ans):
        user = session.query(User).filter(User.id == id).first()
        print(f'{user.name} {user.surname}')


if __name__ == '__main__':
    main()





