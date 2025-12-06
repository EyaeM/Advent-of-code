from itertools import combinations #we live to learn boys.

#This code would probably work but its way too slow and would probably take until the heat death of the universe to compute with 200 lines each with 99 chars
#ive tried other stuff but i dont think it would work so tbh i give up on day 3 part 2

with open('Day 3/sample.txt') as f: lines = f.readlines()
total = 0
lines = [line.strip() for line in lines]

#print(lines)
for link in lines:
    max_wombo = 0
    ntor = len(link) - 12
    for ptor in combinations(range(len(link)), ntor):
        remaining = ''.join(link[i] for i in range(len(link)) if i not in ptor)
        wombocombo = int(remaining)

        if wombocombo > max_wombo:
            max_wombo = wombocombo

    result = str(max_wombo)
    total += int(result)

    print(f"{link} -> {result}") #this is meant to be debugging but its cool so im leaving it in
 
print("Total:",total)