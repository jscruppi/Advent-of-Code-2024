"""

Read the files
seperate into two list that are sorted
compare distances of each index

"""

list1 = []
list2 = []
input_file = open('puzzle_input.txt', 'r')

lines = input_file.readlines()

for line in lines:
    data = line.split('  ')
    list1.append(data[0])
    list2.append(data[1])

list1.sort()
list2.sort()

total_dist = 0
for x in range(len(list1)):
    total_dist += abs( int(list1[x]) - int(list2[x]) )

print(f'Total distance: {total_dist}')

input_file.close()