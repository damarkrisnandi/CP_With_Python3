from collections import defaultdict
def countObj(arr):
    res = defaultdict(int)
    for i in arr:
        res[i]+=1
    
    return res

t = int(input())
while t>0:
    t-=1
    n = input()
    a = list(map(int, input().split(" ")))

    objctd = countObj(a)
    maxx = objctd[min(objctd)]
    for o in objctd:
        if objctd[o] > maxx:
            maxx = objctd[o]
    print(maxx)
