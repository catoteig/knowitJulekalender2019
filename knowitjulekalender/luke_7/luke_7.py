codelist = [13825167, 9216778, 20734802]
init = 5897
maxval = 27644437

def divisjon(day):
    y = -1
    for i in range(2, maxval):
        b = i * day
        rest = b % maxval
        if rest == 1:
            y = i
            break
    z = init * y
    z = z % maxval
    return z


print(divisjon(7))

# Test:
for s in range(0, len(codelist)):
    print('Ok') if divisjon(s+2) == codelist[s] else 'Fail'
