Position = 50
ZeroCount = 0

with open('wandn.txt') as f: 
    lines = f.readlines()

for line in lines:
    distance = int(line[1:])
    old_pos = Position
    
    if "L" in line[0]:
        for step in range(distance):
            Position -= 1
            if Position < 0:
                Position += 100
            if Position == 0:
                ZeroCount += 1
    else:
        for step in range(distance):
            Position += 1
            if Position >= 100:
                Position -= 100
            if Position == 0:
                ZeroCount += 1
    
print("Zerocount:", ZeroCount) #shit code but it works