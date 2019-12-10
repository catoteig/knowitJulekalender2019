from datetime import datetime
import re
import math


def parsedoc(textfile):
    file = open(textfile, 'r')
    list = file.read().splitlines()
    bathlog = {}
    for i in range(0, len(list), 4):
        toalett, sjampo, tannkrem = 0, 0, 0
        row = list[i][:-1] + ' 2018'
        id = datetime.strptime(row, '%b %d %Y')
        for s in range(i+1, i+4):
            if 'toalettpapir' in list[s]:
                toalett = int(re.search(r'\d+', list[s]).group())
            elif 'sjampo' in list[s]:
                sjampo = int(re.search(r'\d+', list[s]).group())
            elif 'tannkrem' in list[s]:
                tannkrem = int(re.search(r'\d+', list[s]).group())
        bathlog[id] = (tannkrem, sjampo, toalett)
    return bathlog


def tottoothpaste(bathlog):
    toothpaste = (x[0] for x in bathlog.values())
    return math.floor(sum(toothpaste) / 125)


def totsjampo(bathlog):
    sjampo = (x[1] for x in bathlog.values())
    return math.floor(sum(sjampo) / 300)


def tottoalettpapir(bathlog):
    toiletpaper = (x[2] for x in bathlog.values())
    return math.floor(sum(toiletpaper) / 25)


def totsjamposun(bathlog):
    sjamposun = []
    for date in bathlog.keys():
        if date.weekday() == 6:
            sjamposun.append(bathlog[date][1])
    return math.floor(sum(sjamposun))


def tottoawed(bathlog):
    toawed = []
    for date in bathlog.keys():
        if date.weekday() == 2:
            toawed.append(bathlog[date][2])
    return math.floor(sum(toawed))


log = parsedoc('logg.txt')
produkt = tottoothpaste(log) * totsjampo(log) * tottoalettpapir(log) * totsjamposun(log) * tottoawed(log)
print(produkt)