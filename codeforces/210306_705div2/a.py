t = int(input())
while t>0:
    t-=1
    n, k = list(map(int, input().split(" ")))
    r = []
    while k>0:
        if (n != k):
            r.append(n)
        n-=1
        k-=1
    
    print(len(r))
    if len(r) > 0:
        print(' '.join(r))
