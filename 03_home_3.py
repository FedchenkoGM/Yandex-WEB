import datetime
import schedule


def kuku(mess, sleep):
    dt = datetime.datetime.now()
    t1, t2 = map(int, sleep.split('-'))
    hour = datetime.datetime.timetuple(dt)[3]
    if not (t1 <= hour <= t2):
        hour %= 12
        if hour == 0:
            hour = 12
        print(mess * hour)


mess = input()
sleep = input()
schedule.every().hour.at(":00").do(kuku(mess, sleep))

while True:
    schedule.run_pending()
