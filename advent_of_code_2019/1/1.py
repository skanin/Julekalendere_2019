import math

f = open('/Users/sanderlindberg/Documents/kodekalendere/advent_of_code_2019/1/inp.txt').readlines()

print("Task 1:")
print(sum(map(lambda x: int(x)//3 - 2, f)))

def foo(elem, summ=0):
    if math.floor(elem/3) - 2 <= 0:
        return summ
    return foo(math.floor(elem/3) - 2, summ+(math.floor(elem/3) - 2))

print()
print("Task 2:")

print(sum(map(lambda x: foo(int(x)), f)))