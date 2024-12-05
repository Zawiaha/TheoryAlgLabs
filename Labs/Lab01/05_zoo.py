#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# есть список животных в зоопарке



# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
# TODO здесь ваш код
def insertElementAtPosition(arrayData, element):
    for data in arrayData:
        print(data)
    elementAfterComeNew = input("Введите элемент, после которого нужно вставить другой элемент: ")
    if(elementAfterComeNew not in arrayData):
        print("Указанный элемент не найден")
        return
    arrayData.insert(arrayData.index(elementAfterComeNew), element)
    return arrayData
# добавьте птиц из списка birds в последние клетки зоопарка

#  и выведите список на консоль
# TODO здесь ваш код
def mergeList(baseList, mergedList):
    return baseList + mergedList
# уберите слона
#  и выведите список на консоль
# TODO здесь ваш код
def removeElementFromList(arrayData, element):
    if element in arrayData:
        arrayData.remove(element)
        print("Удалено!")
        return arrayData
    print("Элемент не найден")
    

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
# TODO здесь ваш код
def getPositionElement(arrayData, element):
    return arrayData.index(element)

def main():
    zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]
    birds = ['rooster', 'ostrich', 'lark', ]
    zoo = insertElementAtPosition(zoo, input("Введите вставляемый элемент: "))
    print(zoo)
    zoo = mergeList(zoo, birds)
    print(zoo)
    zoo = removeElementFromList(zoo, input("Введите убираемый элемент: "))
    print(zoo)
    print(f"lion находится на {getPositionElement(zoo, "lion") + 1} позиции")
    print(f"lark находится на {getPositionElement(zoo, "lark") + 1} позиции")





if __name__ == "__main__":
    main()



