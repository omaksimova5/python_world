# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько
# чисел и строк и сохраните в переменные, выведите на экран.
name = input ('Введите имя')
print(name)

surname = input ('Введите фамилию')
print(surname)

age = input ('Введите возраст')
print(age)

# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате
# чч:мм:сс. Используйте форматирование строк.

sec = int(input('Введите время в секундах'))
hour = sec // 3600
sec %= 3600
minutes = sec // 60
sec %= 60
print('секунды в часах:',hour)
print('секунды в минутах:',min)
print('секунды :',sec)
print('%02d:%02d:%02d' % (hour,min,sec))

# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число
# 3. Считаем 3 + 33 + 333 = 369.

n = int(input("Введите число: "))
number = str(n)
t1 = number + number
t2 = number + number + number
result = n + int(t1) + int(t2)
print("Результат равен:", result)

# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

num = int(input ('Введите число :'))
max = num%10
num = num//10
while num > 0:
    if num%10 > max:
        max = num%10
    num = num//10
print(max)

# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите,
# с каким финансовым результатом работает фирма (прибыль — выручка больше
# издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

revenue = int(input ('Введите выручку : '))
costs = int(input ('Введите затраты : '))
benefit = revenue - costs
print('%.4f' % benefit)
if benefit > 0:
   profit = benefit / revenue
   print('%.4f' % profit)
   personal = int(input('Введите количество сотрудников :'))
   effect = benefit / personal
   print('%.4f' % effect)

# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
#
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
a = int(input('Введите сколько километров пробежал спортсмен :'))
b = int(input('Введите сколько километров составит общий пробег спортсмена :'))
day = 1
while b - a > 0:
    a = a + (a * 0.1)
    day += 1
print(day)