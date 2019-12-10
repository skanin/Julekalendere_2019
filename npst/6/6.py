kode = 'KNO fmw55k8m7i179 z98øyåz8æy67aåy0å6æ7aø1å1438åa5a fmw55k8m7i179 95p11'

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
    '0': '6',
    '1': '7',
    '2': '8',
    '3': '9',
    '4': '0',
    '5': '1',
    '6': '2',
    '7': '3',
    '8': '4',
    '9': '5'
}

for elem in kode:
    if elem in 'wxyzæøå 0123456789':
        dekryptert += dic[elem]
    else:
        dekryptert += chr(ord(elem) + 5)

print(dekryptert)
