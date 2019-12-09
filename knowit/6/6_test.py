from PIL import Image
import numpy as np
import cv2
import io
from stegano import lsb

print(lsb.reveal('/Users/sanderlindberg/Documents/kodekalendere/npst/8/261478b4e6de08c48ef31a93d73f7ea4.jpg'))
'''
im = Image.open('/Users/sanderlindberg/Documents/kodekalendere/npst/8/secret.jpg')
im2 = Image.open('/Users/sanderlindberg/Documents/kodekalendere/npst/8/test.jpg')

im3 = Image.open('/Users/sanderlindberg/Documents/kodekalendere/knowit/6/mush.png')

np_im = np.array(im)
np_im2 = np.array(im2) 
np_im3 = np.array(im3)

rolled = np.roll(np_im, 1, axis=(1))

xor = np.bitwise_xor(rolled, np_im)

img = Image.fromarray(xor)
img.show()'''