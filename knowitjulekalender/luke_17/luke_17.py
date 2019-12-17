import math


def ruller(tall, rulleringer):
    n = str(tall)
    return int((n*2)[rulleringer:len(n)+rulleringer])


def squarenumber(tall):
    root = math.sqrt(tall)
    return True if int(root + 0.5) ** 2 == tall else False


def trianglenumbers(n):
    triangles = [0]
    for i in range(1, n):
        triangles.append((i ** 2 + i)//2)
    return triangles


def runcheck():
    isboth = 0
    list = trianglenumbers(1000000)
    for i in list:
        for j in range(0, len(str(i))):
            t = ruller(i, j)
            if squarenumber(t):
                isboth += 1
                break
    return isboth


print(runcheck())
