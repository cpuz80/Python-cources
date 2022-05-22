##(C) Starodumov Alexei <AlexS>
##посчитать сумму ряда 0 - 88888888
x = 88888888
a = 0
for i in range(0,x+1):
    a = i + a
print('сумма чисел от 0 до ',x, '=', a)
