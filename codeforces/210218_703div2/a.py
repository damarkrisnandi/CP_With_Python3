t = int(input())
while t>0:
    t-=1
    n = int(input())
    H = list(map(int, input().split(" ")))
    for i in range(H):
        if H[i] >= i:
            H[i+1] += (H[i] - i)
    
    
        if len(set(H)) == len(H):
            print("yeS")
        else:
            print("nO")
