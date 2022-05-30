#СЛОВАРЬ, СПИСОК, МНОЖЕСТВО
a = int(input("Вывести примеры использования 1 - Словарь; 2 - Список; 3 - Множество"));
if a == 1:
    print('Использование словаря')
    #добавить в словарь пары ключ+значение
    newdict = {'1997':'Renault Scenic','2003':'Renault Megane','2006':'Renault Clio'}
    #вывести словарь
    print(newdict)
    #получить коллекцию ключей
    print(newdict.keys())
    #получить коллекцию значений
    print(newdict.values())
    #добавить запись в словарь
    newdict['2002'] = 'Renault Laguna'
    #вывести словарь
    print(newdict)
    #заменить значение по ключу
    newdict.update({'2006':'Renault Symbol'})
    #вывести словарь
    print(newdict)
    #удалить ключ (значение тоже очищается)
    del newdict['2002']
    #вывести словарь
    print(newdict)
    #вывод значения по ключу
    print('год выпуска 2006, модель ', newdict.get('2006'))
    #проверить на вхождение ключа в словарь
    searchkey = '2003'
    for keys in newdict.keys():
        if keys == searchkey:
            print('В 2003 году модель - ',newdict.get(keys))
    #вывести пары ключ, значение в цикле
    for key, value in newdict.items():
        print(key, value)
    
if a == 2:
    print('Использование списка')
    #добавим список
    b = ['Renault Scenic','Renault Megane','Renault Clio']
    #вывести список
    print(b)
    #добавить запись в список
    b.append('Renault Laguna')
    #вывести список
    print(b)
    #заменить значение в списке по индексу элемента
    b[2] = 'Renault Symbol'
    #вывести список
    print(b)
    #удалить элемент по индексу
    del b[3]
    #вывести список
    print(b)
    #вывод значения по индексу
    print(b[2])
    #проверить на вхождение в список
    print('Renault Scenic' in b)
    
if a == 3:
    print('Использование множества')
if a not in (1,2,3):
    print('Перезапустите программу и укажите код 1 - 3!')
