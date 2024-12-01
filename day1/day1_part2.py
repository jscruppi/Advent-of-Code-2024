"""

Calculate the singularity score
sim_score = num_left * num_right

-Seperate input into two maps
-Calculate map[x] * map2[x]

"""
from collections import defaultdict

dict1 = defaultdict(int)
dict2 = defaultdict(int)

input_file = open('puzzle_input.txt', 'r')

lines = input_file.readlines()

for line in lines:
    data = line.split('  ')
    dict1[int(data[0])] += 1
    dict2[int(data[1].strip())] += 1

total = 0
for element in dict1:
    total += element * dict2[element]

print(f'Singularity Score: {total}')