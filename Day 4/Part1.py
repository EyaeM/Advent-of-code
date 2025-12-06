with open('Day 4/sample.txt') as f: grid = [line.strip() for line in f.readlines()]
count = 0

#Hello Neighbor. Are you an @?
#Code may be shit but if it works it works

for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] == '@':
            theneighborfromhelloneighbor = 0
            if row > 0 and col > 0 and grid[row-1][col-1] == '@': theneighborfromhelloneighbor += 1
            if row > 0 and grid[row-1][col] == '@': theneighborfromhelloneighbor += 1
            if row > 0 and col < len(grid[row])-1 and grid[row-1][col+1] == '@': theneighborfromhelloneighbor += 1
            if col > 0 and grid[row][col-1] == '@': theneighborfromhelloneighbor += 1
            if col < len(grid[row])-1 and grid[row][col+1] == '@': theneighborfromhelloneighbor += 1
            if row < len(grid)-1 and col > 0 and grid[row+1][col-1] == '@': theneighborfromhelloneighbor += 1
            if row < len(grid)-1 and grid[row+1][col] == '@': theneighborfromhelloneighbor += 1
            if row < len(grid)-1 and col < len(grid[row])-1 and grid[row+1][col+1] == '@': theneighborfromhelloneighbor += 1
            if theneighborfromhelloneighbor < 4:
                count += 1
print("Count:",count)