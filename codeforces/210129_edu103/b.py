from math import floor
t = int(input())
while t>0:
    t-=1
    n,k = list(map(int, input().split(" ")))
    P = list(map(int, input().split(" ")))

    # maxx = P[0]
    # supp = P[1:]
    arr = []
    for p in list(range(len(P))):
        print("p", p)
        if (p != 0):
            print(P[0:p])
            arr.append(sum(P[0:p]))

    print(arr)
    
    # print(res)
    