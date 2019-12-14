def alfabetiser(alfabet, goal):

    newlist = []
    indeks, alfabetindeks, iterations, sevens = 1, 1, 0, 0

    for num in range(0, alfabet[0]):
        newlist.append(alfabet[0])
        iterations += 1

    while iterations >= goal:
        for n in range(0, newlist[indeks]):
            if iterations < 40000000:
                newlist.append(alfabet[alfabetindeks])
            if alfabet[alfabetindeks] == 7:
                sevens += 1
            iterations += 1
        indeks += 1
        alfabetindeks = (1 + alfabetindeks) % len(alfabet)

    return sevens * 7


alfabet = [2, 3, 5, 7, 11]
goal = 217532235

print(alfabetiser(alfabet, goal))
