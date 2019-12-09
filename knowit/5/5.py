st = "tMlsioaplnKlflgiruKanliaebeLlkslikkpnerikTasatamkDpsdakeraBeIdaegptnuaKtmteorpuTaTtbtsesOHXxonibmksekaaoaKtrssegnveinRedlkkkroeekVtkekymmlooLnanoKtlstoepHrpeutdynfSneloietbol"
# 'oep Hlp sla int tno teP mse orm oTt lst'
# st = 'oepHlpslainttnotePmseormoTtlst'

lst = []
for i in range(0, len(st), 3):
    lst.append(st[i:i+3])

for i in range(0, len(lst)//2):
    lst[i], lst[-1-i] = lst[-1-i], lst[i]

lst = list(''.join(lst))

for i in range(1, len(st), 2):
    lst[i], lst[i-1] = lst[i-1], lst[i]

lst[-1], lst[0] = lst[0], lst[-i]
st = ''.join(lst)
st = st[len(st)//2:] + st[0:len(st)//2]
print(st)
'''
length = len(st)
for i in range(0, len(st)//2 + 3, 3):
    first = st[i]
    sec = st[i+1]
    third = st[i+1]
    last = st[length - 1]
    nextToLast = st[length-2]
    nextToLast2 = st[length-3]

    st[i], st[i+1], st[i+2], st[length-3], st[length-2], st[length-1] = nextToLast2, nextToLast, last, first, sec, third
    length -= 3
    # st[i], st[length-3], st[i+1], st[length-2], st[i+2], st[length-1] = st[length-3], st[i], st[length-2], st[i+1], st[length-1], st[i+2]

    st[i+1], st[length-2] = st[length-2], st[i+1]
    st[i+2], st[length-1] = st[length-1], st[i+2]

print(st)
'''

i = 3

# while i != 

print(st)