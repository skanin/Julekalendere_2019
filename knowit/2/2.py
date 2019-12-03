import time
time_start = time.time()

f = open('//Users/sanderlindberg/Documents/kodekalendere/knowit/2/world.txt').read().split("\n")

def find_seq(elem):
    seqs = []
    overflow_ind = 0
    if elem[0] == " ":
        for i in range(len(elem)):
            if elem[i] == "#" or i == len(elem) -1:
                overflow_ind = i
                seqs.append([0, i-1, True])
                break

    if overflow_ind != len(elem) -1:
        for i in range(len(elem)-1):
            start = i
            end = i+1
            overflow = False
            if elem[start] == "#" and elem[end] == " ":
                for j in range(i+1, len(elem)):
                    if elem[j] == " ":
                        end = j
                    elif elem[j] == "#":
                        break
                if end == len(elem) - 1:
                    overflow = True
                seqs.append([start+1, end, overflow])

    return seqs

def calc(arr):
    s = 0
    for i in range(len(t)):
        for j in range(len(t[i])):
            if t[i][j][2] == False:
                if t[i][j][0] == 0 or t[i][j][0] == 1:
                    s += t[i][j][1]
                else:
                    s += t[i][j][1] - t[i][j][0] + 1

    return s

t = []
count = 0
for elem in f:
    if count == 0:
        t.append(find_seq(elem))
        count += 1
    else:
        if t[-1] == []:
            break
        t.append(find_seq(elem))

print(time.time() - time_start)
print(calc(t))
