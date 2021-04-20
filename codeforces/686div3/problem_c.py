from collections import defaultdict
def countObj(arr):
    res = defaultdict(int)
    for i in arr:
        res[i]+=1
    
    return res

tests = int(input())
for t in range(tests):
    n = int(input())
    arr = input()
    arr2 = countObj([int(i) for i in arr.split(" ")])
    a = -1
    cek = arr.split(str(min([arr2[i] for i in arr2])))
    for i in arr2:
        if arr2[i] == min([arr2[i] for i in arr2]):
            a = i

    cek = arr.split(str(i))
    for c in cek:
        if c != "":
            jml +=1
    print(jml)