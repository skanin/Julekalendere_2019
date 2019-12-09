import png
from urllib.request import urlopen
import ssl
from itertools import chain
from PIL import Image

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
'''
f = Image.open('/Users/sanderlindberg/Documents/kodekalendere/knowit/6/mush.png')

pix = f.load()

print(f.size)

print(pix[274, 182])

tmp = []

for i in range(f.size[1]):
    elem = []
    for j in range(f.size[0]):
        elem.append(pix[j, i])
    tmp.append(elem)

xored = [[tmp[0][0]]]
for elem in tmp:
    for i in range(len(elem)):
        last_xored = xored[-1][-1]
        toXor = elem[i]
        xored[-1].append([toXor[0]^last_xored[0], toXor[1]^last_xored[1], toXor[2]^last_xored[2]])
'''


# '/Users/sanderlindberg/Documents/kodekalendere/knowit/6/mush.png'
f = png.Reader(file=urlopen('https://knowit-julekalender.s3.eu-central-1.amazonaws.com/2019-luke6/mush.png', context=ctx))

print(list(f.read()))
rowcols = list(f.read()[2])[::-1]
# rowcols = [[[240, 33, 11], [205, 111, 102], [120, 96, 7], [45, 3, 202], [76, 237, 47]], [[123, 33, 11], [205, 111, 102], [120, 96, 7], [45, 3, 202], [76, 237, 47]]]
decimal = []


for i in range(len(rowcols)):
    tmp = []
    for j in range(0, len(rowcols[i]), 3):
        tmp.append([rowcols[i][j], rowcols[i][j+1], rowcols[i][j+2]])
    decimal.append(tmp)

decimal_copy = decimal.copy()

print(decimal[0][0])

'''
for i in range(len(rowcols)):
    tmp = []
    for j in range(0, len(rowcols[i]), 3):
        tmp.append([rowcols[i][j], rowcols[i][j+1], rowcols[i][j+2]])
    decimal.append(tmp)
'''

xored = [[decimal[0][0]]]
'''
print(decimal[0][0])
print(decimal[0][1])
# decimal[] = rad
# decimal[][] = kolonne
# decimal[][][] = punkt.
# [[[1, 2, 3], [3, 4, 5], [6,7,8]]. [[1, 2, 3], [1, 2, 3], [6,7,8]]]
for i in range(0, len(decimal)):
    for j in range(0, len(decimal[i])):
        if j == 0 and len(xored) > 1:
            xored[-1].append([decimal[i][j][0]^xored[-2][-1][0], decimal[i][j][1]^xored[-2][-1][1], decimal[i][j][2]^xored[-2][-1][2]])
        else:
            xored[-1].append([decimal[i][j][0]^xored[-1][-1][0], decimal[i][j][1]^xored[i-1][-1][1], decimal[i][j][2]^xored[-1][-1][2]])
    xored.append([])

print(xored[0][1])
xored_proc = []
for col in xored:
    tmp = []
    for row in col:
        for elem in row:
            tmp.append(elem)
    xored_proc.append(tmp)
'''

for i in range(len(decimal_copy)):
    for j in range(1, len(decimal_copy[i])):
        last_xored = xored[-1][-1]
        now = decimal_copy[i][j]
        xored[-1].append([now[0]^last_xored[0], now[1]^last_xored[1], now[2]^last_xored[2]])
    if i < len(decimal_copy):
        xored.append([now])

print(xored[-1])


xored_proc = []
for col in xored:
    tmp = []
    for row in col:
        for elem in row:
            tmp.append(elem)
    if len(tmp) == 825:
        xored_proc.append(tmp)

f2 = open('xored.png', 'wb')
w = png.Writer(275, 183, greyscale=False)
w.write(f2, xored_proc)
f2.close()

png.from_array(xored_proc, 'L').save("small_smiley.png")
