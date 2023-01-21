import datetime
import schedule


def kuku():
    dt = datetime.datetime.now()
    hour = datetime.datetime.timetuple(dt)[3] % 12
    if hour == 0:
        hour = 12
    print("Ку" * hour)


schedule.every().hour.at(":00").do(kuku)

while True:
    schedule.run_pending()
