from PIL import Image


def dekrypter(picture):

    im = Image.open(picture)
    pixels = list(im.getdata())
    pixels.reverse()
    pixels.append([0, 0, 0])
    x1 = pixels[0]
    xx, result = [], []

    for i in range(1, len(pixels)):
        x0 = pixels[i]
        for j in range(0, len(pixels[i])):
            xx.append(x1[j] ^ x0[j])
        result.append(tuple(xx))
        x1 = x0
        xx = []
    result.reverse()

    im.putdata(result)
    im.show()

    return result


dekrypter('mush.png')
