'''
 Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек;
* до часа: <m> мин <s> сек;
'''

time_duration = int(input("Введите продолжительность времени в секундах: "))
hours = time_duration // 3600
minutes = (time_duration // 60) % 60
seconds = time_duration % 60
if minutes < 10:
    minutes = str('0'+ str(minutes))
else:
    minutes = str(minutes)
if seconds < 10:
    seconds = str('0' + str(seconds))
else:
    seconds = str(seconds)
print(str(hours) + ':' + str(minutes) + ':' + str(seconds))