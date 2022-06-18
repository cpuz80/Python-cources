# #поиск в списке
animals = ['Dog', 'Cat', 'Bird', 'Fish']
# #простейшие случаи
# #искомая константа
elem = 'Bird'
#
# #перебор элементов в списке
for animal in animals:
    #проверка на соответствие
     if animal == elem:
         print(animal, ' Найдено!')

# #через оператор in
if elem in animals: print(elem, ' Найдено!')

# #с помощью лямда-функции
retrieved_elements = list(filter(lambda x: elem in x, animals))
print(retrieved_elements, ' Найдено!')

# #используя метод count
if animals.count(elem) > 0:
    print(elem, ' Найдено!')
#
# #через внешний модуль (как надо было в задании))
import Lection3Module as mymod
for s in animals:
    print(s,elem, mymod.funcld(s,elem))