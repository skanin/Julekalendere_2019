import requests
import shutil
import os
from PIL import Image
# site = requests.get('https://verksted.npst.no/verksted.npst.no.2c3ecc69.js/').text.split(';')[32][66:-1:].split(",")

# site = map(lambda x: (requests.get('https://verksted.npst.no/images/' + x[1:-1] + ".png", stream=True), x), site)

# distinct_imgs = set(map(lambda x: Image.open('/Users/sanderlindberg/Documents/kodekalendere/npst/7/bilder/' + x), os.listdir('/Users/sanderlindberg/Documents/kodekalendere/npst/7/bilder')


'''
print('Hey1')
site2 = map(lambda x: x.content, site)
print('Hey2')
site3 = filter(lambda x: x.content not in site2, site)
print('hey3')
print(list(site3))
'''
'''
for img in site:
    local_file = open('/Users/sanderlindberg/Documents/kodekalendere/npst/7/bilder/' + img[1] + '.png', 'wb')
    img[0].raw.decode_content = True
    shutil.copyfileobj(img[0].raw, local_file)
'''
'''
unike = []
count = 0

for img in site:
    count += 1
    if len(unike) == 0:
        unike.append(img)
    else:
        for i in unike:
            if i.content != img.content:
                unike.append(img)
    print(f'{count}/12202')
'''
'''
for elem in site:
    i += 1
    img = requests.get('https://verksted.npst.no/images/' + elem[1:-1] + ".png")
    if len(unike) == 0:
        unike.append(img)
    for lst in unike:
        if img.content != lst.content:
            unike.append(img)
    
    print(f'{i}/{len(site)}')
print(unike)
'''

# img1 = requests.get('https://verksted.npst.no/images/09fa082d154fbcc8132d9758d625a6b1.png')
# img2 = requests.get('https://verksted.npst.no/images/b5a477dbcc1c33e3f5d9ad08774eb97d.png')

# print(img1.content == img2.content)
# site = site[site.find('module.exports=')+15:]