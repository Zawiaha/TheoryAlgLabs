from itertools import combinations
def threeDigitCombinations(d):
    for combo in combinations(d, 3):
        if combo[0] == "0":
            continue
        yield int(''.join(combo))
def generateFunctionValues(a, b, func):
    x = a
    while x <= b:
        yield func(x)
        x += 0.01
def getSort(d):
    return [d[key] for key in sorted(d.keys(), reverse=True)]

def printDigitCombination():
    number = "0123456789"
    gen = threeDigitCombinations(number)
    for _ in range(50):
        print(next(gen))

def printFunctionValues():
    a = -20
    b = 100
    f = lambda x: -1.5 * x + 2
    gen = generateFunctionValues(a, b, f)
    for _ in range(20):
        print(next(gen))

def printSortedDict():
    d = {'cat': 'кот', 'horse': 'лошадь', 'tree': 'дерево', 'dog': 'собака', 'book': 'книга'}
    sortedValues = getSort(d)
    print(sortedValues)