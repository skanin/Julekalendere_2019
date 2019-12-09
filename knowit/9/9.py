import requests

def findKrampus(n):
    n_squared = str(n**2)
    for i in range(len(n_squared)-1):
        a = int(n_squared[0:i+1])
        b = int(n_squared[i+1::])

        if (a + b == n) and (a != 0 and b != 0):
            return True
    return False

print(sum(map(int, filter(lambda x: findKrampus(int(x)), open('krampus.txt').readlines()))))
