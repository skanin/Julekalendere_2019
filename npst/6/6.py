import requests
import hashlib

kode = 'KNO fmw55k8m7i179 z98øyåz8æy67aåy0å6æ7aø1å1438åa5a fmw55k8m7i179 95p11'
kode1 = 'KNO fmwggkymyioån 30å6ø8432æå54710a9æ09a305å7z9829 fmwggkymyioån ngpoo'
gammel_kode = 'KNO fmw55k8m7i179 z98øyåz8æy67aåy0å6æ7aø1å1038åa5a fmw55k8m7i179 95p11'

dic = {
    'v': 'æ',
    'w': 'ø',
    'x': 'å',
    'y': 'a',
    'z': 'b',
    'æ': 'c',
    'ø': 'd',
    'å': 'e',
    ' ': ' ',
    '5': 'l',
    '8': 'a',
    '7': 'e',
    '9': 's',
    '1': 't'
}

new = ''
# newcode = 'aed1ff57d2d38f783665bca4027a485f'
newcode = 'bsadaebaca6efea0e6cefdtet43aeflf'
for ch in kode:
    if ch in 'vwxyzæøå ':
        new += dic[ch]
    elif ch in '2346015789':
        new += ch
    else:
        new += chr(ord(ch) + 5)

print(new)

# hashlib.md5(str.encode())

f = open('/Users/sanderlindberg/Desktop/juleord.txt', 'r').read().split('\n')

def md5(st):
    return hashlib.md5(st.encode()).hexdigest()

for elem in f:
    if md5(elem.capitalize()) == '6d9ed9fad247e18e28c1a0203367b61f': 
        print(md5(elem.capitalize()), elem.capitalize())
print(md5('b98daeb8ca67fea0e6c7fd1e1438ef5f'))
'''
count = {
    '0': 0,
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0,
    '7': 0,
    '8': 0,
    '9': 0
}

summ = 0
for ch in kode:
    if ch in '0123456789':
        count[ch] += 1
        summ += 1

print(count)
print(summ)

diff = [[], []]

for i in range(len(kode)):
    if kode[i] !=gammel_kode[i]:
        diff[0].append((i, kode[i])) 
        diff[1].append((i, gammel_kode[i]))

print(diff)
dic = {
    'v': 'æ',
    'w': 'ø',
    'x': 'å',
    'y': 'a',
    'z': 'b',
    'æ': 'c',
    'ø': 'd',
    'å': 'e',
    ' ': ' ',
    '0': 'o',
    '1': 'l',
    '5': 's',
    '3': 'e',
    '4': 'a',
    '7': 't'
}
tmp = 'z98øyåz8æy67aåy0å6æ7aø1å1438åa5a'
new = ''
'''
'''
for ch in kode:
    if ch in 'vwxyzæøå ':
        new += dic[ch]
    elif ch == '5':
        new += dic['1']
    elif ch == '8':
        new += dic['4']
    elif ch == '9':
        new += dic['5']
    elif ch == '1':
        new += dic['7']
    elif ch == '7':
        new += 'e'
    elif ch in '2346':
        new += ch
    else:
        new += chr(ord(ch) + 5)
'''
'''
for ch in kode1:
    if ch in 'vwxyzæøå ':
        new += dic[ch]
    elif ch in '0123456789':
        new += ch
    else:
        new += chr(ord(ch) + 5)
'''
'''
for ch in tmp:
    if ch in '0123456789':
        new += ch
    elif ch in 'vwxyz':
        new += dic[ch]
    else:
        new += ch
'''
'''
print(new)

digits = {
    '0': '5',
    '1': '6',
    '2': '7',
    '3': '8',
    '4': '9',
    '5': '0',
    '6': '1',
    '7': '2',
    '8': '3',
    '9': '4'
}

newnew = ''
for elem in new:
    if elem in '0123456789':
        newnew += digits[elem]
    else:
        newnew += elem

print(f'{newnew=}')
'''
'''
tmp = 'z98øyåz8æy67aåy0å6æ7aø1å1438åa5a'

# xyzæøåabcdefgh
newdic = {
    'e': 'å',
    'd': 'ø',
    'b': 'z',
    'c': 'æ',
    'a': 'y'
}
newnew = ''
for elem in tmp:
    if elem in 'æøå':
        newnew += dic[elem]
    elif elem in newdic.keys():
        newnew += newdic[elem]
    else:
        newnew += elem

print(newnew)
    
'''