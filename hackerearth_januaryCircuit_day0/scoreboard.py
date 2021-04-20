t = int(input())
while t>0:
    t-=1
    q = int(input().split(" ")[1])
    a = input().split(" ")
    a.append("0")
    for i in range(q):
        [l, r] = input().split(" ")
        a[int(l)-1] = r
        print(len(list(set(a))))