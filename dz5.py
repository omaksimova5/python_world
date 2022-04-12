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
