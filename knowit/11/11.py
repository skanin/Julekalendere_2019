import requests

f = requests.get('https://julekalender.knowit.no/resources/2019-luke11/terreng.txt').text


speed = 10703437
'''
i = 0
while speed > 0 and i < len(f):
    if f[i] == 'I':
        speed += 12
        count = 1
        while f[i+1] == 'I':
            i += 1
            count += 1
            speed += 12*count
    elif f[i] == 'F':
        speed -= 35
        i += 2
    else:
        if f[i] == 'G':
            speed -= 27
        elif f[i] == 'A':
            speed -= 59
        elif f[i] == 'S':
            speed -= 212
        i += 1
'''
count = 1
last = 'Q'
km = 0
# f='IIGGFFAIISGIFFSGFAAASS'
# speed = 300
f_in_row = 0
for i in range(len(f)):
    if last == 'I' and f[i] == 'I':
        speed += 12*count
        count += 1
    elif last == 'F' and f[i] == 'F':
        speed += 35
        f_in_row += 1
    else:
        if f[i] == 'G':
            speed -= 27
        elif f[i] == 'I':
            speed += 12
            count += 1
        elif f[i] == 'A':
            speed -= 59
        elif f[i] == 'S':
            speed -= 212
        elif f[i] == 'F':
            f_in_row += 1
            speed -= 70
    last = f[i]
    print(f_in_row)
    if f[i] != 'I':
        f_in_row = 0
        count = 1
    if speed <= 0:
        km = i + 1
        #print(speed, last)
        break
    #print(speed, last)
    

print(km)