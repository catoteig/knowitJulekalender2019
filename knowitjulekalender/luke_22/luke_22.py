def counttrees(txt):
    file = open(txt, 'r')
    list = file.read().splitlines()
    height = 0

    y = len(list) - 1
    for x in range(len(list[y])):
        if list[y][x] == '#':
            height += treeheight(list, x)

    return round(height * 200)


def treeheight(list, x):
    y = len(list)
    for i in range(y):
        if list[i][x] == '#':
            return (y - i) * 0.2


print('Test OK') if counttrees('forest_test.txt') == 2120 else print('Test fail')
print(counttrees('forest.txt'))
