import datetime

date = datetime.date(2026,8,23)

today = datetime.date.today()
print(today)
print(date)


time = datetime.time(22,7,00)
now = datetime.datetime.now().strftime("%H %M %S")

print(now)


target_datetime = datetime.datetime(2030,1,2,12,30,1)
current_time = datetime.datetime.now()

passed_time = target_datetime-current_time
print(passed_time)