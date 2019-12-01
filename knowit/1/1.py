f = [int(i) for i in open('/Users/sanderlindberg/Documents/Knowit_Julekalender_2019/1/inp.txt').read().split(',')]

dragon_size = 50

sheep_left = 0

number_of_days_without_grow = 0

days = 0

for sheep in f:
    sheep_available = sheep + sheep_left
    
    if sheep_available > dragon_size:
        sheep_left = sheep_available - dragon_size 
        dragon_size += 1
        number_of_days_without_grow = 0
    elif sheep_available == dragon_size:
        sheep_left = sheep_available - dragon_size 
        dragon_size += 1
        number_of_days_without_grow = 0
    elif sheep_available < dragon_size:
        dragon_size -= 1
        sheep_left = 0
        number_of_days_without_grow += 1
    
    if number_of_days_without_grow == 5:
        break
    days += 1

print(days)
