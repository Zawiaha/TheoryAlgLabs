def getInputMovie():
    movies = input("Ввод названий фильмов через запятую: ")
    if len(movies) > 2:
        return movies
    else:
        return 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

def extractMoviesPosition(moviesString):
    delimeterPosition = []
    for i in range(len(moviesString)):
        if moviesString[i] == ',':
            delimeterPosition.append(i)
    return delimeterPosition

def cutString(moviesString, delimeterPosition):
    iter = 0
    movies = []
    for i in delimeterPosition:
        movies.append(moviesString[iter:i])
        iter = i + 2
    movies.append(moviesString[iter: len(moviesString)])
    return movies
def showMovies(movies):
    print(movies[0] + '\n',
          movies[-1] + '\n',
          movies[1] + '\n',
          movies[-2]
          )

if __name__ == "__main__":
    moviesString = getInputMovie()
    showMovies(cutString(moviesString, extractMoviesPosition(moviesString)))