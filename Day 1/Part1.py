Position = 50
Count = 0
ZeroCount = 0

with open('wandn.txt') as f: lines = f.readlines()

num_lines = len(lines)

for line in lines:
    Count += 1
    print(line)
    if "L" in line[0]:
        #print("L Found")
        Position -= int(line[1:])
    else:
        #print("R Found")
        Position += int(line[1:])
    Position = Position % 100
    if Position == 0:
        ZeroCount += 1
print(ZeroCount)