def ishidden(number):
    s = str(number)
    sr = s[::-1]
    s2 = str(number + int(sr))
    return True if s != sr and s2 == s2[::-1] else False


def sumhidden(first, last):
    total = 0
    for i in range(first, last):
        if ishidden(i):
            total += i
    return total


print('Test 1 OK') if ishidden(38) else print('Test 1 fail')
print('Test 2 OK') if not ishidden(49) else print('Test 2 fail')
print(sumhidden(1, 123454321))
