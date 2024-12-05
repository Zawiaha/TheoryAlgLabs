#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Создайте списки:
# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
# список списков приблизителного роста членов вашей семьи
# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

def inputData():
    my_family = []
    my_family_height = []
    for i in range(int(input("Введите количество человек в семье: "))):
        data = input("Введите имя и рост в формате (NAME:HEIGHT): ").split(':')
        my_family.append(data[0])
        my_family_height.append([data[0], data[1]])
    return my_family_height
def showInfoFamily(familyHeiht):
    for i in familyHeiht:
        if i[0].lower() == "отец":
            print(f"Рост отца - {i[1]} см")
            break
    else:
        print("Отец не найден")
    print(f"Общий рост семьи - {sum(int(member[1]) for member in familyHeiht)}")

if __name__ == "__main__":
    showInfoFamily(inputData())
   
    













