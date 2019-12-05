import csv

days = 0
size = 50
spare = 0
dead = 0

with open('csv.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for LIST in reader:
        for RAD in LIST:
            if dead >= 5:
                print('Død, overlevde i ', days - 1, ' dager')
                break
            total = int(RAD) - size + spare
            if total >= 0:
                size += 1
                days += 1
                spare = total
                dead = 0
            else:
                size -= 1
                days += 1
                spare = 0
                dead += 1
