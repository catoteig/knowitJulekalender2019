import csv
import operator


def runall(csvfile, charfile):
    charlist = parsecharlist(charfile)
    finalnames = {}
    with open(csvfile, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for employee in reader:

            gender = employee[2]

            p = 0 if gender == 'M' else 1
            modulo = sumascii(employee[0]) % len(charlist[p])
            name_1 = charlist[p][modulo]

            split = splitname(employee[1])
            modulo = sumletternumber(split[0]) % len(charlist[2])
            name_2 = charlist[2][modulo]

            if gender == 'M':
                s = prodascii(split[1]) * len(employee[0])
            else:
                s = prodascii(split[1]) * (len(employee[0]) + len(employee[1]))
            s = int(''.join(sorted(str(s), reverse=True)))
            name_3 = charlist[3][s % len(charlist[3])]

            fullname = '%s %s%s' % (name_1, name_2, name_3)
            if fullname in finalnames:
                finalnames[fullname] += 1
            else:
                finalnames[fullname] = 1
    return finalnames


def splitname(string):
    length = len(string)
    split_1 = string[0:length // 2 + (length % 2 > 0)]
    split_2 = string[length // 2 + (length % 2 > 0):]
    return [split_1, split_2]


def parsecharlist(txtfile):
    parsedlist, templist = [], []
    file = open(txtfile, 'r')
    list = file.read().splitlines()
    for row in list:
        if row == '---':
            parsedlist.append(templist)
            templist = []
        else:
            templist.append(row)
    parsedlist.append(templist)
    return parsedlist


def sumascii(word):
    total = 0
    for i in range(0, len(word)):
        total += ord(word[i])
    return total


def prodascii(word):
    product = 1
    for i in range(0, len(word)):
        product *= ord(word[i])
    return product


def sumletternumber(word):
    total = 0
    for i in range(0, len(word)):
        m = 64 if word[i].isupper() else 96
        total += (ord(word[i]) - m)
    return total


def findmax(dictionary):
    return max(dictionary.items(), key=operator.itemgetter(1))[0]


print('Test OK') if runall('employees_test.csv', 'names.txt') == {'Poe Lightverse': 1} else print('Test fail')
print(findmax(
    runall('employees.csv', 'names.txt')
))
