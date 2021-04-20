from collections import defaultdict
def countObj(arr):
    res = defaultdict(int)
    for i in arr:
        res[i]+=1
    
    return res

t = int(input())
while t>0:
    t-=1
    ls = int(input())
    s1 = input()
    s2 = input()

    s1_cts = countObj(s1)
    s2_cts = countObj(s2)
    s1s2 = set.union(set(s1_cts), set(s2_cts))
    res = "YES"
    arr_res = []
    for s in s1s2:
        arr_res.append(s1_cts[s] - s2_cts[s])
    
    # cek = list(set(arr_res))
    # cek.sort()
    if (countObj(arr_res)[-1] == 1 and countObj(arr_res)[1] == 1) or countObj(arr_res)[0] == len(arr_res):
        res = "YES"
    else:
        res = "NO"
    print(res)