t = int(input())
while t>0:
    t-=1
    n = input()
    a = list(map(int, input().split(" ")))

    min_a = min(a)
    amin = list(map(lambda x: x - min_a, a))
    filter_amin = list(filter(lambda x: x > 0, amin))
    print(len(filter_amin))
    
