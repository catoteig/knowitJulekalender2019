def fillwater(txt):
    file = open(txt, 'r')
    list = file.readlines()
    water = 0
    for row in list:
        i = -1
        first = -1
        while True:
            i = row.find('#', i + 1)
            if i == -1:
                break
            if first >= 0 and i >= 0 and (i - first) != 1:
                water += i - first - 1
            first = i
    print(water)


fillwater('world.txt')
