sec = int(input('Введите время в секундах'))
hour = sec // 3600
sec %= 3600
min = sec // 60
sec %= 60
print('секунды в часах:',hour)
print('секунды в минутах:',min)
print('секунды :',sec)
print('%02d:%02d:%02d' % (hour,min,sec))

