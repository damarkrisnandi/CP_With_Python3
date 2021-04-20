t = int(input())
while t>0:
    t-=1
    q,d = list(map(int, input().split(" ")))
    A = list(map(int, input().split(" ")))
    list_base = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    list_check = list(map(lambda x: x*d, list_base))
    for a in A:
        cek = list(filter(lambda x: a - x >= 0 and ((a - x)%10 == 0), list_check))
        if (len(cek) > 0):
            print("YES")
        else:
            print("NO")