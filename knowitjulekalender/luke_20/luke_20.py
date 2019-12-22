import math


def dowork(iterations):
    tasks = [0, 0, 0, 0, 0]
    direction = True
    nextelf, currelf, step, nextstep = 0, -1, 0, 0

    while step < iterations:

        nextelf = moveelf(currelf, direction)
        nextstep = step + 1
        if checkprime(nextstep) and findmin(tasks) >= 0:
            nextelf = findmin(tasks)
        elif nextstep % 28 == 0:
            direction = not direction
            nextelf = moveelf(currelf, direction)
        elif nextstep % 2 == 0 and ismax(nextelf, tasks):
            nextelf = moveelf(nextelf, direction)
        elif nextstep % 7 == 0:
            nextelf = 4

        tasks[nextelf] += 1
        currelf = nextelf
        step = nextstep

    return max(tasks) - min(tasks)


def moveelf(currentelf, direction):
    return (currentelf + 1) % 5 if direction else (currentelf - 1) % 5


def findmin(list):
    result = []
    for i, y in enumerate(list):
        if y == min(list):
            result.append(i)
    return -1 if len(result) > 1 else result[0]


def findmax(list):
    result = []
    for i, y in enumerate(list):
        if y == max(list):
            result.append(i)
    return -1 if len(result) > 1 else result[0]


def ismax(elf, list):
    return True if findmax(list) == elf else False


def checkprime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(number)) + 1, 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False
    return True


print(dowork(1000740))
