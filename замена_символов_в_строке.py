##(C) Starodumov Alexei <AlexS>
##Заменить в строке "asdxfghyxyx" все буквы "х" на "у"
##громоздко получилось(
a = 'asdxfghyxyx'
sym = ''
newsym = ''
newstring = ''
##строку в массив
mass = list(a)
##обходим массив
while mass:
    sym = mass.pop()
    ##проверка на условие замены
    if sym == "x":
      newsym = "y"
      newstring = newstring + newsym
    else:
      newstring = newstring + sym
reverse = list(newstring)
##пересобрать строку
newstring = ''
while reverse:
	sym = reverse.pop()
	newstring = newstring + sym
print(newstring)
    
    
