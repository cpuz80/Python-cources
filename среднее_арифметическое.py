##(C) Starodumov Alexei <AlexS>
##Среднее арифметическое ряда [3, 4, 56, 100, 2, 2, 3]
L = [3, 4, 56, 100, 2, 2, 3]
s = 0
summS = 0
eq = 0
result = 0
while L:
    ##получаем список поэлементно
    s = L.pop()
    ##суммируем поэлементно
    summS = summS + s
    ##считаем количество элементов
    eq = eq+1
#выводим результат
print('среднее арифметическое ряда =', summS/eq)

    
