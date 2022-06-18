# #поиск в списке
animals = ['Dog', 'Cat', 'Bird', 'Fish']
# #простейшие случаи
# #искомая константа
ELEM = 'Bird'
#
# #перебор элементов в списке
for animal in animals:
    # проверка на соответствие
    if animal == ELEM:
        print(animal, ' Найдено!')

# #через оператор in
if ELEM in animals: print(ELEM, ' Найдено!')

# #с помощью лямда-функции
retrieved_elements = list(filter(lambda x: ELEM in x, animals))
print(retrieved_elements, ' Найдено!')

# #используя метод count
if animals.count(ELEM) > 0:
    print(ELEM, ' Найдено!')
#
# #через мой внешний модуль (как надо было в задании))
import Lection3Module as mymod

for s in animals:
    print(s, ELEM, mymod.funcld(s, ELEM))

# через внешнюю библиотеку
import Levenshtein as ExtLibLev

for s in animals:
    print(s, ELEM, ExtLibLev.setratio(s, ELEM))