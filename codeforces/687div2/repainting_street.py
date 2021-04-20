from collections import defaultdict
import math
def countObj(arr):
    res = defaultdict(int)
    for i in arr:
        res[i]+=1
    
    return res

def inputArray():
    return list(map(int,input().strip().split()))
  
def solve():
    n,k = inputArray()
    houses = inputArray()
    count_color = countObj(houses)
    max_count = 0
    base_color = 0
    days = 0
    for i in count_color:
        if count_color[i] == max(count_color.values()):
            max_count = count_color[i]
            base_color = i
            break

    cek2 = " ".join("".join(list(map(str,houses)))).split(str(base_color))
    for c in cek2:
        if c != " ":
            days += 1
    print(days)



tests = int(input())
for t in range(tests):
    solve()