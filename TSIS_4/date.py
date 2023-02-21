# import datetime
# from datetime  import timedelta

# # 1
# def subtract_from_now(n):
#     return datetime.datetime.now()-datetime.timedelta(days = n)

# print(datetime.datetime.now())
# day = int(input())
# print(subtract_from_now(day))

# # 2
# today = datetime.date.today()
# print("tommorow: ",today - datetime.timedelta(days = -1))
# print("today: ", today)
# print("yesterday: ",today - datetime.timedelta(days = 1))
# print(datetime.datetime.fromtimestamp(1))# 1970-01-01 06:00:01

# # 3
# now = datetime.datetime.now()
# print(now)
# drop_second = now - datetime.timedelta(microseconds=day)
# print(drop_second)

# # 4

# tday = datetime.date.today()
# bday = datetime.date(2023, 11, 11)

# till_bday = bday - tday
# print(till_bday.total_seconds())
# print(till_bday.days)

import datetime

dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)

tdelta = datetime.timedelta(days = 7)
hdelta = datetime.timedelta(hours = 12)
print(dt)
print(dt.date()) # or time()
print(dt.year) # days, hour, second ....
print(dt + tdelta)
print(dt + hdelta)


dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()
print(dt_today)
print(dt_now)
print(dt_utcnow)
