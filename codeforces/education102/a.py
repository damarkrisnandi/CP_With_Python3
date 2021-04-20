t = int(input())
while t>0:
    ans = "NO"
    t-=1
    n, d = list(map(int, input().split(" ")))
    a = list(map(int, input().split(" ")))
    big = list(filter(lambda o : o > d, a))
    if len(big) == 0:
        ans = "YES"
    else:
        a2 = a
        a2.sort()
        if a2[0] + a2[1] > d:
            ans = "NO"
        else:
            ans = "YES"

    print(ans)