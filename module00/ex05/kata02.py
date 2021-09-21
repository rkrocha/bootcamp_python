import datetime


t = (3, 30, 2019, 9, 25)


hour, mins, year, month, day = t
print(f'{month:02}/{day:02}/{year} {hour:02}:{mins:02}')


date_format = str(t)[1:-1]
print(datetime.datetime.strptime(date_format, '%H, %M, %Y, %m, %d'))
