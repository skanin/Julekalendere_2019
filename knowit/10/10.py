f = map(lambda x: x.strip('\t\n'), open('logg.txt', 'r').readlines())

def getNum(st):
    ant = ''
    for elem in st[2::]:
        if elem.isalpha():
            return int(ant)
        ant += elem
    return int(ant)


new_day = True
tannkrem = 0
sjampo = 0
dopapir = 0
sjampo_son = 0
dopapir_ons = 0
days = ['man', 'tir', 'ons', 'tor', 'fre', 'lør', 'søn']

day = -1
for line in f:
    if line.startswith('*'):
        if 'tannkrem' in line:
            tannkrem += getNum(line)
        elif 'sjampo' in line:
            sjampo += getNum(line)   
            if days[day] == 'søn':
                sjampo_son += getNum(line)
        elif 'toalettpapir' in line:
            dopapir += getNum(line)
            if days[day] == 'ons':
                dopapir_ons += getNum(line)
    else:
        if day == 6:
            day = 0
        else:
            day += 1

print((dopapir//25)*dopapir_ons*(tannkrem//125)*sjampo_son*(sjampo//300))