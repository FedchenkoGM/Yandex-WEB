from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs
from data.departments import Department


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init('db/mars_explorer.sqlite')
#    app.run()
    session = db_session.create_session()

    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.hashed_password = "cap"
    session.add(user)

    user = User()
    user.surname = "Weir"
    user.name = "Andy"
    user.age = 18
    user.position = "chief scientist"
    user.speciality = "geologist"
    user.address = "module_1"
    user.email = "andy_chief@mars.org"
    user.hashed_password = "sci"
    user.set_password(user.hashed_password)
    session.add(user)

    user = User()
    user.surname = "Watny"
    user.name = "Mark"
    user.age = 25
    user.position = "middle scientist"
    user.speciality = "biologist"
    user.address = "module_2"
    user.email = "mark@mars.org"
    user.hashed_password = "bio"
    user.set_password(user.hashed_password)
    session.add(user)

    user = User()
    user.surname = "Kapoor"
    user.name = "Venkat"
    user.age = 15
    user.position = "pilot"
    user.speciality = "pilot, navigator"
    user.address = "module_2"
    user.email = "kapoor@mars.org"
    user.hashed_password = "pilot"
    user.set_password(user.hashed_password)
    session.add(user)

    user = User()
    user.surname = "Sanders"
    user.name = "Teddy"
    user.age = 27
    user.position = "programmer"
    user.speciality = "IT specialist"
    user.address = "module_2"
    user.email = "sanders@mars.org"
    user.hashed_password = "comp"
    user.set_password(user.hashed_password)
    session.add(user)

    user = User()
    user.surname = "Bean"
    user.name = "Sean"
    user.age = 17
    user.position = "chief engineer"
    user.speciality = "builder"
    user.address = "module_1"
    user.email = "bean@mars.org"
    user.hashed_password = "build"
    user.set_password(user.hashed_password)
    session.add(user)

    job = Jobs()
    job.team_leader = 1
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2, 3'
    job.is_finished = False
    session.add(job)

    job = Jobs()
    job.team_leader = 2
    job.job = 'exploration of mineral resources'
    job.work_size = 15
    job.collaborators = '4, 3, 6'
    job.is_finished = True
    session.add(job)

    job = Jobs()
    job.team_leader = 3
    job.job = 'development of a management system'
    job.work_size = 25
    job.collaborators = '5'
    job.is_finished = False
    session.add(job)

    job = Jobs()
    job.team_leader = 4
    job.job = 'analysis of atmospheric air samples'
    job.work_size = 15
    job.collaborators = '4, 5'
    job.is_finished = False
    session.add(job)

    job = Jobs()
    job.team_leader = 5
    job.job = 'Mars Rover maintenance'
    job.work_size = 5
    job.collaborators = '4'
    job.is_finished = True
    session.add(job)

    job = Jobs()
    job.team_leader = 6
    job.job = 'preventive vaccinations of the crew'
    job.work_size = 7
    job.collaborators = '3'
    job.is_finished = False
    session.add(job)

    department = Department()
    department.title = "Department of transportation"
    department.chief = 4
    department.email = "transport@mars.org"
    department.members = "26, 37, 19"
    session.add(department)

    department = Department()
    department.title = "Department of construction"
    department.chief = 6
    department.email = "build@mars.org"
    department.members = "16, 17, 28"
    session.add(department)

    department = Department()
    department.title = "Department of of construction_2"
    department.chief = 6
    department.email = "build_2@mars.org"
    department.members = "9, 13, 18"
    session.add(department)

    department = Department()
    department.title = "Department of biological research"
    department.chief = 3
    department.email = "bio@mars.org"
    department.members = "7, 10, 11"
    session.add(department)

    department = Department()
    department.title = "Department of geological exploration"
    department.chief = 2
    department.email = "geo@mars.org"
    department.members = "6, 8, 12"
    department = session.query(Department).filter(Department.id == 1).first()
    department.members = '3, 4, 5'
    session.add(department)

    session.commit()



if __name__ == '__main__':
    main()