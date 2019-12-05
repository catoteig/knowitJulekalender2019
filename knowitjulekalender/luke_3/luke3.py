from PIL import Image

bitlist = list(map(int, open("img.txt").read()))

img = Image.new("1", (1287, 567))
img.putdata(bitlist)
img.save("ikea.png")
img.show()
