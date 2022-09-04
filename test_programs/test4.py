# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190

heros=['spider man','thor','hulk','iron man','captain america']

count = 0

for i in heros:
    count += 1
# print(count)

heros.append('black panther')

heros.remove('black panther')
heros.insert(3, 'black panther')

heros[1:3] = ['doctor strange']
print(heros)

heros.sort()



max_number = int(input())
numbers = [number for number in range(1, max_number+1) if number % 2 != 0 ]
print(numbers)