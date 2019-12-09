import re
import time

start = time.time()

wheels = {
    '0': ['PLUSS101', 'OPP7', 'MINUS9', 'PLUSS101'],
    '1': ['TREKK1FRAODDE', 'MINUS1', 'MINUS9', 'PLUSS1TILPAR'],
    '2': ['PLUSS1TILPAR', 'PLUSS4', 'PLUSS101', 'MINUS9'],
    '3': ['MINUS9', 'PLUSS101', 'TREKK1FRAODDE', 'MINUS1'],
    '4': ['ROTERODDE', 'MINUS1', 'PLUSS4', 'ROTERALLE'],
    '5': ['GANGEMSD', 'PLUSS4', 'MINUS9', 'STOPP'],
    '6': ['MINUS1', 'PLUSS4', 'MINUS9', 'PLUSS101'],
    '7': ['PLUSS1TILPAR', 'MINUS9', 'TREKK1FRAODDE', 'DELEMSD'],
    '8': ['PLUSS101', 'REVERSERSIFFER', 'MINUS1', 'ROTERPAR'],
    '9': ['PLUSS4', 'GANGEMSD', 'REVERSERSIFFER', 'MINUS9']
}

def setOriginalWheels():
    global wheels
    wheels = {
    '0': ['PLUSS101', 'OPP7', 'MINUS9', 'PLUSS101'],
    '1': ['TREKK1FRAODDE', 'MINUS1', 'MINUS9', 'PLUSS1TILPAR'],
    '2': ['PLUSS1TILPAR', 'PLUSS4', 'PLUSS101', 'MINUS9'],
    '3': ['MINUS9', 'PLUSS101', 'TREKK1FRAODDE', 'MINUS1'],
    '4': ['ROTERODDE', 'MINUS1', 'PLUSS4', 'ROTERALLE'],
    '5': ['GANGEMSD', 'PLUSS4', 'MINUS9', 'STOPP'],
    '6': ['MINUS1', 'PLUSS4', 'MINUS9', 'PLUSS101'],
    '7': ['PLUSS1TILPAR', 'MINUS9', 'TREKK1FRAODDE', 'DELEMSD'],
    '8': ['PLUSS101', 'REVERSERSIFFER', 'MINUS1', 'ROTERPAR'],
    '9': ['PLUSS4', 'GANGEMSD', 'REVERSERSIFFER', 'MINUS9']
}

def pluss(elem, cmd):
    return elem + int(cmd[re.search(r"\d", cmd).start()::])

def minus(elem, cmd):
    return elem - int(cmd[re.search(r"\d", cmd).start()::])

def opp(elem):
    while int(str(elem)[-1]) != 7:
        elem += 1
    return elem

def gangmsd(elem):
    return elem * int(str(elem)[0]) if elem > 0 else elem * int(str(elem)[1])

def delemsd(elem):
    return elem // int(str(elem)[0]) if elem > 0 else elem // int(str(elem)[1])

def reversersiffer(elem):
    return int(str(elem)[::-1]) if elem > 0 else int('-' + str(elem)[::-1][:-1])

def pluss1tilpar(elem):
    if elem < 0:
        tmp = str(elem)[1::]
    else:
        tmp = str(elem)
    
    new_el = ''
    for digit in tmp:
        if not (int(digit) % 2):
            new_el += str(int(digit) + 1)
        else:
            new_el += digit
    
    return int(new_el) if elem > 0 else -int(new_el)

def trekk1fraodde(elem):
    if elem < 0:
        tmp = str(elem)[1::]
    else:
        tmp = str(elem)
    
    new_el = ''
    for digit in tmp:
        if int(digit) % 2:
            new_el += str(int(digit) - 1)
        else:
            new_el += digit
    
    return int(new_el) if elem > 0 else -int(new_el)

def roten(key):
    new_list = []
    lst = wheels[key]
    length = len(lst)
    for i in range(1, length):
        new_list.append(lst[i])
    
    new_list.append(lst[0])
    
    return new_list

def roter(cmd):
    cmd = cmd[5::]
    for key in wheels:
        new_list = roten(key)
        if cmd == 'ALLE':
            wheels[key] = new_list
        elif cmd == 'PAR' and not (int(key) % 2):
            wheels[key] = new_list
        elif cmd == 'ODDE' and (int(key) % 2):
            wheels[key] = new_list

def getNextCmd(elem):
    return wheels[str(elem)][0]

def calcwinnings(coins, cmd):
    if cmd == 'STOPP':
        return coins
    elif cmd == 'PLUSS4' or cmd == 'PLUSS101':
        result = pluss(coins, cmd)
    elif 'MINUS' in cmd:
        result = minus(coins, cmd)
    elif cmd == 'REVERSERSIFFER':
        result = reversersiffer(coins)
    elif cmd == 'OPP7':
        result = opp(coins)
    elif cmd == 'GANGEMSD':
        result = gangmsd(coins)
    elif cmd == 'DELEMSD':
        result = delemsd(coins)
    elif cmd == 'PLUSS1TILPAR':
        result = pluss1tilpar(coins)
    elif cmd == 'TREKK1FRAODDE':
        result = trekk1fraodde(coins)
    elif 'ROTER' in cmd:
        roter(cmd)
        wheels[str(coins)[-1]] = roten(str(coins)[-1])
        return calcwinnings(coins, getNextCmd(str(coins)[-1]))
    else:
        result = ''
    wheels[str(coins)[-1]] = roten(str(coins)[-1])
    return calcwinnings(result, getNextCmd(str(result)[-1]))

def main():
    start = time.time()
    winnings = []

    for i in range(0, 10):
        setOriginalWheels()
        if i != 9:
            winnings.append(calcwinnings(i+1, wheels[str(i+1)][0]))
        else:
            winnings.append(calcwinnings(i+1, wheels[str(0)][0]))
    return time.time() - start



for i in range(0, 100):


    