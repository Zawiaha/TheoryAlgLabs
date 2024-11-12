import math

def calcSquare(radius):
    """Расчет площади круга"""
    return round(math.pi * math.pow(radius, 2), 4)

def calcDistanceToPoint(point):
    """Расчет расстояния от точки до начала координат"""
    return math.sqrt(float(point[0]) ** 2 + float(point[1]) ** 2)

def isPointIndside(point, radius):
    """Проверка нахождения точки в области круга"""
    return calcDistanceToPoint(point) <= radius

def getRadius():
    """Получение радиуса круга от пользователя"""
    return float(input("Введите радиус круга:"))

def getPoint():
    """Получение располочение точки"""
    return (input("Введите координаты точки (Формат: x-y)")).split('-')

def main():
    radius = getRadius()
    coordPoint = getPoint()
    print(f"Площадь круга: {calcSquare(radius)}")
    print(f"Нахождение в точки в области круга радиусом {radius} - {isPointIndside(coordPoint, radius)}")
    
if __name__ == "__main__":
    main()


