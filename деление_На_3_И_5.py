##(C) Starodumov Alexei <AlexS>
##Сосчитать произведение чисел [3, 4, 56, 100, 15, 2, 20, 30], 
##кратных и 3 и 5.
A = [3, 4, 56, 100, 15, 2, 20, 30]
p = 0
x=1
##обходим список
while A:
    ##извлекаем элемент списка
    p = A.pop()
    ##проверяем на делимость на 3 и 5
    if p%3 == 0 and p%5 == 0:
        ##условие выполнено, перемножаем
        x = x * p
print(x)
            
