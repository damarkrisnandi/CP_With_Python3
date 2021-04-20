from math import ceil
t = int(input())
while t>0:
    t-=1
    n,k = list(map(int, input().split(" ")))
    if n > k:
        mult = int(ceil(n/k))
        k = k * mult

    print(int(ceil(k/n)))