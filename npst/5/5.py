from itertools import product, combinations, combinations_with_replacement
import requests

commands = product('✨⚡🔑', repeat=9)

print(commands)

print("Start")
for elem in commands:
    data = {'commands': ''.join(elem)}
    r = requests.get('https://npst.no/api/%F0%9F%99%83.js', data)
    if '>🚩<' in r.json()['state']:
        print(elem)
        print(r.json()['message'])
print("Done")