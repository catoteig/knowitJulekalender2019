def findnumber(integer):
    s = str(integer)
    target, it = 0, 0
    for i in range(1, 11):
        if s == str(i) * 4:
            return 0
    while not target == 6174:
        sort = sorted(s, reverse=True)
        s = ''.join(sort)
        target = int(s) - int(s[::-1])
        s = str(target).zfill(4)
        it += 1
    return it


def iterate(first, last):
    seven = 0
    for i in range(first, last):
        seven += 1 if findnumber(i) == 7 else 0
    return seven


print('Test OK') if findnumber(1000) == 5 else print('Test fail')
print(iterate(1000, 9999))
