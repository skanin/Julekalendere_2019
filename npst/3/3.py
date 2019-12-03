kode = 'KNO fmwggkymyioån 30å6ø8432æå54710a9æ09a305å7z9829 fmwggkymyioån ngpoo'

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

for elem in kode:
    if elem in 'wvxyzæøå ':
        dekryptert += dic[elem]
    elif elem in '0123456789':
        dekryptert += elem
    else:   
        dekryptert += chr(ord(elem) + 5)

print(dekryptert)