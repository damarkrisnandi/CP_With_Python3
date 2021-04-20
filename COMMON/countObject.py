from collections import defaultdict
def countObj(arr):
    res = defaultdict(int)
    for i in arr:
        res[i]+=1
    
    return res