def sail(txt, startpos):
    pos = startpos
    direction = True
    changedir = 1
    newlist = []

    file = open(txt, 'r')
    list = file.read().splitlines()
    listlength = len(list[0])

    for row in list:
        newlist.append(row.ljust(listlength, '0'))

    while True:
        if pos[0] == listlength:
            break
        if findland(pos[0], pos[1], direction, newlist):
            direction = not direction
            changedir += 1
            pos = [pos[0] + 1, pos[1]]
        else:
            pos = move(pos, direction)

    return changedir


def move(pos, direction):
    if direction:
        return [pos[0] + 1, pos[1] - 1]
    else:
        return [pos[0] + 1, pos[1] + 1]


def findland(x, y, direction, list):
    if direction:
        return True if list[y - 3][x] == '#' else False
    else:
        return True if list[y + 3][x] == '#' else False


print('Test OK') if sail('test.txt', [1, 9]) == 5 else print('Test fail')
print(sail('fjord.txt', [1, 44]))