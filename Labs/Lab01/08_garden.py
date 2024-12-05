#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
# TODO здесь ваш код
def flowersInSet(gardenData, meadowData):
    gardenSet = set(gardenData)
    meadowSet = set(meadowData)
    return gardenSet, meadowSet

def flowersInfo(gardenData, meadowData):
    print(f"Цветы на лугу: {gardenData}")
    print(f"Цветы на лугу: {meadowData}")
    print(f"Цветы, которые растут в саду и на лугу: {gardenData & meadowData}") 
    print(f"Цветы, которые растут в саду, но не растут на лугу: {gardenData - meadowData}")
    print(f"Цветы, которые растут на лугу, но не растут в саду: {meadowData - gardenData}")

gardenSet, meadowSet = flowersInSet(garden, meadow)
flowersInfo(gardenSet, meadowSet)

# выведите на консоль все виды цветов
# TODO здесь ваш код

# выведите на консоль те, которые растут и там и там
# TODO здесь ваш код

# выведите на консоль те, которые растут в саду, но не растут на лугу
# TODO здесь ваш код

# выведите на консоль те, которые растут на лугу, но не растут в саду
# TODO здесь ваш код
