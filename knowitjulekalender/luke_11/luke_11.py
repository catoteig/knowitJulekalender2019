testresult = 11
startspeed = 10703437


def landing(txt, vstart):
    vs, vi, fjell = vstart, 1, False
    with open(txt) as fileobj:
        for line in fileobj:
            for ch in range(0, len(line)):
                vn = line[ch]
                v1 = line[ch + 1] if ch < len(line) - 1 else ''
                if vs <= 0:
                    break
                elif vn == 'F':
                    vs += -70 if fjell else 35
                    fjell = False if fjell else True
                elif vn == 'I':
                    vs += delta(vn) * vi
                    vi = 1 if not v1 == 'I' else vi + 1
                else:
                    vs += delta(vn)
        return ch


def delta(groundtype):
    cases = {
        'G': - 27,
        'I': 12,
        'A': -59,
        'S': -212,
        'F1': -70,
        'F2': 35
    }
    return cases.get(groundtype)


print('Test OK') if landing('terrengtest.txt', 300) == testresult else print('Test fail')

print(landing('terreng.txt', startspeed))