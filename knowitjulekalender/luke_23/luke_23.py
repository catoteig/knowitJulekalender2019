import math


def harshad(minval, maxval):
    ant = 0
    for i in range(minval, maxval + 1):
        s = str(i)
        h = 0
        for n in range(len(s)):
            h += int(s[n])
        if i % h == 0 and isprime(h):
            ant += 1
    return ant


def isprime(number):
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


def runtest():
    assert harshad(1729, 1729) == 1
    assert harshad(1730, 1730) == 0


runtest()
print(harshad(1, 98765432))
