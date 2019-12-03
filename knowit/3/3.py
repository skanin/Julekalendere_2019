from PIL import Image

data = list(map(int, open('/Users/sanderlindberg/Documents/kodekalendere/knowit/3/img.txt').read()))

img = Image.new('1', (1287, len(data)//1287), "black")
img.putdata(data)
img.show()
