import json


def parsejson(jsonfile):
    parsedjson = {}

    with open(jsonfile, 'r') as f:
        maze = json.load(f)
        for z in maze:
            for q in range(0, len(z)):
                parsedjson[(z[q]['x'], z[q]['y'])] = z[q]
    return parsedjson


def movenext(x, y, jsonfile, order):
    mazemap = parsejson(jsonfile)
    visited, previous = {}, []
    visited[(x, y)] = True

    while not x == 499 or not y == 499:
        tupp = (mazemap[(x, y)])
        changedvalue = False
        for g in order:
            x1, y1 = x, y
            if g == 'aust':
                x1 = x + 1
            elif g == 'vest':
                x1 = x - 1
            elif g == 'nord':
                y1 = y - 1
            elif g == 'syd':
                y1 = y + 1
            if not tupp[g]:
                if not (x1, y1) in visited:
                    changedvalue = True
                    previous.append((x, y))
                    x, y = x1, y1
                    visited[(x, y)] = True
                    break
        if not changedvalue:
            temp = previous.pop()
            x, y = temp[0], temp[1]

    return len(visited)


order1 = ['syd', 'aust', 'vest', 'nord']
order2 = ['aust', 'syd', 'vest', 'nord']
a = (movenext(0, 0, 'MAZE.JSON', order1))
b = (movenext(0, 0, 'MAZE.JSON', order2))

print(abs(a - b))
