with open("Day 2/sample.txt") as f:lines = f.read().split(",")
BadTotal = 0
#print("lines", lines) Debugging stuff

for idk in lines:
    start_str, end_str = map(int, idk.split("-"))
    
    for n in range(start_str, end_str + 1):
        s = str(n)
        for length in range(1, len(s) // 2 + 1):
            #print("S:",s)
            #print("N:",n)
            #print("L:",length)
            if s[:length] * (len(s) // length) == s:
                BadTotal += n
                break

print ("Bad Total is :",BadTotal)