def highest_grossing(yearFrom, yearUpto, genre):
    f = open('IMDB_reviews.csv', 'r')
    head = f.readline().strip().split(',')

    nameIndex = head.index('name')
    yearIndex = head.index('year')
    genreIndex = head.index('genre')
    grossIndex = head.index('gross')

    maxGrossing = 0
    maxGrossingMovie = ''

    while True:
        line = f.readline().strip()
        if not line:
            break
        l = line.split(',')
        if l[yearIndex] != '' and yearFrom <= int(l[yearIndex]) <= yearUpto and genre in l[genreIndex]:
            if l[grossIndex] != '' and int(l[grossIndex]) > maxGrossing:
                maxGrossing = int(l[grossIndex])
                maxGrossingMovie = l[nameIndex]
    f.close()
    return maxGrossingMovie
