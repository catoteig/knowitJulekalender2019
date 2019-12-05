import csv
import time

log = {}


def logcord(x, y):

    cord = str(x) + '.' + str(y)

    if cord in log:
        log[cord] = log[cord]+1
    else:
        log[cord] = 1


def summasummarum(dict):

    sum = 0

    for value in dict:
        for i in range(0, dict[value] + 1):
            sum += i
    return sum


def plotgraph(csvfile):

    x, y = 0, 0

    with open(csvfile, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            while True:
                if x < int(row[0]):
                    x += 1
                    logcord(x, y)
                    continue
                elif x > int(row[0]):
                    x -= 1
                    logcord(x, y)
                    continue
                elif y < int(row[1]):
                    y += 1
                    logcord(x, y)
                    continue
                elif y > int(row[1]):
                    y -= 1
                    logcord(x, y)
                    continue
                break


plotgraph('luke_4/coords.csv')
print(summasummarum(log))
