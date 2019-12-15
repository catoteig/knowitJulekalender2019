def finnvolum(trekant):

    trekant1 = trekant[0:3]
    trekant2 = trekant[3:6]
    trekant3 = trekant[6:9]

    vollist = []
    vollist.append(trekant1[0] * trekant2[1] * trekant3[2])
    vollist.append(- (trekant1[0] * trekant3[1] * trekant2[2]))
    vollist.append(- (trekant2[0] * trekant1[1] * trekant3[2]))
    vollist.append(trekant2[0] * trekant3[1] * trekant1[2])
    vollist.append(trekant3[0] * trekant1[1] * trekant2[2])
    vollist.append(- (trekant3[0] * trekant2[1] * trekant1[2]))
    total = sum(vollist) / 6

    return total


def lagtrekantliste(line):

    list = []
    for x in line.split(','):
        list.append(float(x))
    return list


def runall(csvfile):

    file = open(csvfile)
    list = file.readlines()

    volumlist = []
    for row in list:
        trekant = lagtrekantliste(row)
        trekant = finnvolum(trekant)
        volumlist.append(trekant)
    volumlist = round(sum(volumlist) / 1000, 3)

    return volumlist


print('Test OK') if runall('TEST.CSV') == 0.167 else print('Test fail')
print(runall('MODEL.CSV'))
