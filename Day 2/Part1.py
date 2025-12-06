with open("Day 2/sample.txt") as f:lines = f.read().split(",")
BadTotal = 0
# print("lines", lines) Debugging styuff

for idk in lines:
    start_str, end_str = map(int, idk.split("-"))
    
    for n in range(start_str, end_str + 1):
        s = str(n)
        HalfLength1 = len(str(start_str))
        HalfLength2 = len(str(end_str))
        
        #print(HalfLength1,HalfLength2) 
        #print(s)
        
        if len(s) % 2 == 0:
            HalfLength = len(s) // 2
            if s[:HalfLength] == s[HalfLength:]:
                BadTotal += n

print ("Bad Total is :",BadTotal)