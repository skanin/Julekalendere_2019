
from PIL import Image
import matplotlib.image as mpimg 
import matplotlib.pyplot as plt 
import requests
import cv2
import io

im = Image.open('/Users/sanderlindberg/Documents/kodekalendere/npst/8/secret.jpg')
output = io.BytesIO()
im.save(output, format='JPEG')

hex_data = output.getvalue()
print(hex_data[:100])
'''
im = cv2.imread('/Users/sanderlindberg/Documents/kodekalendere/npst/8/strava.png')
im = cv2.bitwise_xor(im)

plt.imshow(im)
plt.show()
'''
'''
import numpy as np
import matplotlib.pyplot as plt

arr = (plt.imread('/Users/sanderlindberg/Documents/kodekalendere/npst/8/strava.png') * 255).astype(int)
shape = arr.shape
arr = arr.reshape(-1, shape[-1])

for i in range(arr.shape[0] - 1, 0, -1):
    arr[i] ^= arr[i-1]

plt.imshow(np.reshape(arr, shape))
plt.show()

'''
'''
def extractPalette(infile,outfile):
    im=Image.open(infile)
    pal=im.palette.palette
    if im.palette.rawmode!='RGB':
        raise ValueError("Invalid mode in PNG palette")
    output=open(outfile,'wb')
    output.write('RIFF\x10\x04\x00\x00PAL data\x04\x04\x00\x00\x00\x03\x00\x01') # header
    output.write(''.join(pal[i:i+3]+'\0' for i in range(0,768,3))) # convert RGB to RGB0 before writing 
    output.close()

extractPalette(f, 'test.png')

'''
