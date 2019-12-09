kode = 'KNO fmwggkymyioån 30å6ø8432æå54710a9æ09a305å7z9829 fmwggkymyioån ngpoo'
kode1 = 'KNO fmw55k8m7i179 z98øyåz8æy67aåy0å6æ7aø1å1038åa5a fmw55k8m7i179 95p11'
kode2 = '30e6d8432ce54710f9c09f305e7b9829'

dekryptert = ''

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
    '0': '4',
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

leet = {
    'u': 'æ',
    'v': 'ø',
    'w': 'å',
    'x': 'a',
    'y': 'b',
    'z': 'c',
    'æ': 'd',
    'ø': 'e',
    'å': 'f',
    ' ': ' ',
    '0': 'o',
    '1': 't',
    '2': 'z', #Elr R
    '3': 'e',
    '4': 'a',
    '5': 'l',
    '6': 'g',
    '7': 'e',
    '8': 'a',
    '9': 's'
}


for elem in kode:
    if elem in 'wxyzæøå ':
        dekryptert += dic[elem]
    elif elem in '0123456789':
        dekryptert += elem
    else:
        dekryptert += chr(ord(elem) + 5)

print(dekryptert)
dekryptert2 = ''
for elem in 'PST krø55p8r7n179 b98daeb8ca67fea0e6c7fd1e1038ef5f krø55p8r7n179 95u11':
    if elem in 'wxyzæøå ':
        dekryptert2 += dic[elem]
    elif elem in '0123456789':
        dekryptert2 += leet[elem]
    else:
        dekryptert2 += elem

print(dekryptert2)