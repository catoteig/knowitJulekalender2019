import matplotlib.pyplot as plt


def drawcoords(txtfile):
    list_x, list_y = parsecharlist(txtfile)

    for i in range(len(list_x)):
        plt.plot(list_x[i], list_y[i], 'ro')
        plt.axis('off')
        plt.title('Tur %s' % i)
        plt.show()


def parsecharlist(txtfile):
    x, y, x_temp, y_temp = [], [], [], []
    file = open(txtfile, 'r')
    list = file.read().splitlines()

    for row in list:
        if row == '---':
            x.append(x_temp)
            y.append(y_temp)
            x_temp, y_temp = [], []
        else:
            s = row.split(',')
            x_temp.append(int(s[0]))
            y_temp.append(int(s[1]))
    x.append(x_temp)
    y.append(y_temp)

    return x, y


drawcoords('turer_test.txt')
drawcoords('turer.txt')
