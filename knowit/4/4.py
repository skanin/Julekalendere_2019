import time

start = time.time()

f = list(map(lambda x: x.split(','), open('/Users/sanderlindberg/Documents/kodekalendere/knowit/4/coords.csv', 'r').read().split('\n')[1:-1]))

visited = {'[0, 0]': -1}
last = list()

def checkVisited(elem):
    if str(elem) in visited:
        visited[str(elem)] += 1
    else:
        visited[str(elem)] = 1
    return visited[str(elem)]

def handleNegativeX(lst, x, y, mins):
    if last != [x, y]:
        mins += checkVisited([x, y])
    if int(lst[0]) == x:
        return x, mins
    return handleNegativeX(lst, x-1, y, mins)

def handleNegativeY(lst, x, y, mins):
    if last != [x, y]:
        mins += checkVisited([x, y])
    if int(lst[1]) == y:
        return y, mins
    return handleNegativeY(lst, x, y-1, mins)

def handlePositiveX(lst, x, y, mins):
    if last != [x, y]:
        mins += checkVisited([x, y])
    if int(lst[0]) == x:
        return x, mins
    return handlePositiveX(lst, x+1, y, mins)

def handlePositiveY(lst, x, y, mins):
    if last != [x, y]:
        mins += checkVisited([x, y])
    if int(lst[1]) == y:
        return y, mins
    return handlePositiveY(lst, x, y+1, mins)

x = 0
y = 0
mins = 0
for elem in f:
    if int(elem[0]) < x:
        x, mins = handleNegativeX(elem, x, y, mins)
    elif int(elem[0]) > x:
        x, mins = handlePositiveX(elem, x, y, mins)

    last = [x, y]

    if int(elem[1]) < y:
        y, mins = handleNegativeY(elem, x, y, mins)
    elif int(elem[1]) > y:
        y, mins = handlePositiveY(elem, x, y, mins)
    
    last = [x, y]

print(f'Tok: {(time.time() - start)*1000} ms')
print(mins)