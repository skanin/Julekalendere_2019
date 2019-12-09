# Algoritme: 
# For alle tall y fra 2 tilogmed 27644436
# 
# 1. 
#   a) kalkuler b = y * x
#   b) kalkuler r = b % 27644437, altså r = rest(b / 27644437)
#   c) Dersom resten r er 1, har en funnet y = y' = 1 ⎾ x
# 2. 
#   Kalkuler z = 5897 * y.
# 3.
#   Koden for dag x er resten til z / 27644437, altså z % 27644437.
# 
# 
# Merknad: Alle restene er positive. Dersom resten er negativ, legg til 27644437 inntil resten er positiv.
#


print((5897 * list(map(lambda y: int((y*2)%27644437), [i for i in range(2, 27644437)])).index(1)-3)%27644437)


def calc(x):
    for y in range(2, 27644437):
        b = y * x
        r = b % 27644437

        if r == 1:
            print(f'{r=} {x=} {y=}')

'''
    for y in range(2, 2764437):
        b = y * x
        r = int(b % 27644437)
        while r < 0:
            r += 27644437
        if r == 1:
            z = 5897 * y
            return z % 27644437
'''
'''
for i in range(2, 8):
    print(calc(i))
'''