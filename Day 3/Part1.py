with open('Day 3/sample.txt') as f: lines = f.readlines()
total = 0
lines = [line.strip() for line in lines]

#print(lines)
for link in lines:
    max_wombo = 0
    #print(line)
    
    for pie in range(len(link) - 1):
        largest_after = max(link[pie+1:])
        wombocombo = int(link[pie] + largest_after)

        if wombocombo > max_wombo:
            max_wombo = wombocombo

    result = str(max_wombo)
    total += int(result)

    print(f"{link} -> {result}") #this is meant to be debugging but its cool so im leaving it in

print("Total:",total)