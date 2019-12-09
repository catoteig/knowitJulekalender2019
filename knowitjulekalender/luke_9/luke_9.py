def findkrampus(txt):
    file = open(txt, 'r')
    numlist = file.readlines()
    result = []
    for row in numlist:
        if krampustest(row):
            result.append(int(row))
    krampustotal = sum(result)
    return krampustotal


def krampustest(testtall):
    num = str(int(testtall) ** 2)
    result = False
    for i in range(0, len(num)-1):
        tall1, tall2 = int(num[0:i+1]), int(num[i+1:len(num)])
        if tall1 == 0 or tall2 == 0:
            break
        elif (tall1 + tall2) == int(testtall):
            result = True
    return result


print('Test OK') if findkrampus('krampus2.txt') == 45 else print('Test fail')
print(findkrampus('krampus.txt'))
