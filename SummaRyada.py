# посчитать сумму ряда от 0 до введенного
x = int(input('Укажите целое число: '))
import numpy as np
y = np.array(range(x))
z = sum(y)
#  z = np.mean(y)
print(y, z)

# сгенерировать список из 100 случайных чисел и просуммировать
items = np.random.randint(100, size=100000)
import pprint
print('Вывести сумму из 100 случайных чисел: ')
pprint.pprint(items)
print(sum(items))