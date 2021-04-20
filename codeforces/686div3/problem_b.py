from collections import defaultdict
def countObj(arr):
    res = defaultdict(int)
    for i in arr:
        res[i]+=1
    
    return res

def inputPar():
    array = input()
    return [int(i) for i in array.split(" ")]

tests = int(input())
for t in range(tests):
    n_par = int(input())
    par = inputPar()
    result = countObj(par)
    yes = -1
    for i in result:
        if result[i] == 1:
            yes = result[i]
            break
    if yes == -1:
        print(-1)
    else:
        print(par.index(yes) + 1)