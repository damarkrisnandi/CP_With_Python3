tests = int(input())
for t in range(tests):
    line1 = input().split(" ")
    size = int(line1[0])
    subsequences = int(line1[1])
    binaryS = input()
    all1 = len(binaryS) == binaryS.count('1')
    all0 = len(binaryS) == binaryS.count('0')
    n = 0
    for subs in range(subsequences):
        linesubs = input().split(" ")
        idxsubs1 = int(linesubs[0])
        idxsubs2 = int(linesubs[1])

        s = binaryS[idxsubs1 - 1:int(linesubs[1])]
        leftright = binaryS.split(s)
        n = leftright[0].count(s[0:1]) + leftright[1].count(s[len(s)-1:len(s)])

        if s == binaryS:
            print("NO")
        elif (all1 or all0):
            print("YES")
        elif n >= 1:
            print("YES")
        else:
            print("NO")
        

        
