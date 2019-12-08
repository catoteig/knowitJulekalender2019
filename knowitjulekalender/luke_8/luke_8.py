import math

state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def operasjon(x):
    return{
        0: [pluss101, opp7, minus9, pluss101],
        1: [trekk1fraodde, minus1, minus9, pluss1tilpar],
        2: [pluss1tilpar, pluss4, pluss101, minus9],
        3: [minus9, pluss101, trekk1fraodde, minus1],
        4: [roterodde, minus1, pluss4, roteralle],
        5: [gangemsd, pluss4, minus9, stopp],
        6: [minus1, pluss4, minus9, pluss101],
        7: [pluss1tilpar, minus9, trekk1fraodde, delemsd],
        8: [pluss101, reversersiffer, minus1, roterpar],
        9: [pluss4, gangemsd, reversersiffer, minus9]
    }[x]


def pluss4(inn):
    return inn + 4


def pluss101(inn):
    return inn + 101


def minus9(inn):
    return inn - 9


def minus1(inn):
    return inn - 1


def reversersiffer(inn):
    temp = str(inn)
    if temp[0] == '-':
        temp = temp[1:len(temp)]
        return - int(temp[::-1])
    else:
        return int(temp[::-1])


def opp7(inn):
    temp = str(inn)
    while not temp[-1] == '7':
        inn += 1
        temp = str(inn)
    return inn


def gangemsd(inn):
    temp = str(inn)
    temp = temp[0] if not temp[0] == '-' else temp[1]
    result = inn * int(temp)
    return result

def delemsd(inn):
    temp = str(inn)
    temp = temp[0] if not temp[0] == '-' else temp[1]
    result = inn / int(temp)
    return math.floor(result)


def pluss1tilpar(inn):
    temp = str(inn)
    result = ''
    for s in range(0, len(temp)):
        if temp[s] == '-':
            result += temp[s]
        elif int(temp[s]) % 2 == 0:
            result += str(int(temp[s]) + 1)
        else:
            result += str(temp[s])
    return int(result)


def trekk1fraodde(inn):
    temp = str(inn)
    result = ''
    for s in range(0, len(temp)):
        if temp[s] == '-':
            result += temp[s]
        elif not int(temp[s]) % 2 == 0:
            result += str(int(temp[s]) - 1)
        else:
            result += str(temp[s])
    return int(result)


def roterpar(inn):
    for s in range(0, len(state)):
        if s % 2 == 0:
            state[s] += 1
    return inn


def roterodde(inn):
    for s in range(0, len(state)):
        if not s % 2 == 0:
            state[s] += 1
    return inn


def roteralle(inn):
    for s in range(0, len(state)):
        state[s] += 1
    return inn


def stopp(inn):
    global stopp
    stopp = False
    return inn


def roter(indeks):
    state[indeks] += 1


def playgame(initvalue):
    saldo = initvalue
    while True:
        temp = str(saldo)
        temp = temp[len(temp)-1]
        temp = int(temp)
        if state[temp] % 4 == 3 and temp == 5:
            break
        saldo = operasjon(temp)[state[temp] % 4](saldo)
        roter(temp)
    return saldo


result = []

for g in range (1, 11):
    result.append(playgame(g))
    state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print(max(result))