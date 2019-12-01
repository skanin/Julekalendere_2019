import exrex
import hashlib
import random

regex = r'[*@!#%&()^~{}][0-9][A-Z][a-z]'

print("Oppgave 2: ")

alle = list(filter(lambda x: sum(list(map(lambda y: ord(y), x))) % 128 == 24, list(exrex.generate(regex))))

print(alle[random.randint(0, len(alle))])

print("\n"*2 + "Oppgave 3:")

for elem in alle:
    if hashlib.sha1(elem.encode()).hexdigest() == '42f82ae6e57626768c5f525f03085decfdc5c6fe':
        print(elem)