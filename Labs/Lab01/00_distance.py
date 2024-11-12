import math

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

#Расчет расстояния на координатной сетке
def calcDistance(cord1, cord2):
    return math.sqrt(math.pow((cord1[0] - cord2[0]), 2) + math.pow((cord1[1] - cord2[1]), 2)) 
#Ввод расположения городов на координатной сетке
def inputLocation():
    sites = {}
    sitesCount = int(input("Кол-во городов: "))
    for i in range(sitesCount):
        inpSites = input("Название города и координаты. Формат - CityName x:y ")
        sites[inpSites.split(' ')[0]] = (int(inpSites.split(' ')[1].split(':')[0]), int(inpSites.split(' ')[1].split(':')[1]))
        print(f"Город {inpSites.split(' ')[0]} добавлен!")
    return sites
#Заполнение словаря расстояний между городами
def fillDistance(sites):
    distance = {}
    for city1, coord1 in sites.items():
        distance[city1] = {}
        for city2, coord2 in sites.items():
            if city1 != city2:
                distance[city1][city2] = round(calcDistance(coord1, coord2), 2)
    return distance
#Вывод расстояний
def showDistance(distance):
    print("Расстояния между городами:")
    for city, dests in distance.items():
        for dest, distance in dests.items():
            print(f"{city} -> {dest}: {distance} км")

def main():
    showDistance(fillDistance(inputLocation()))

if __name__ == "__main__":
    main()


