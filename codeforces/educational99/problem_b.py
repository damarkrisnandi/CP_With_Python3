def solve():
    x = int(input())
    i1 = 1
    i2 = 1
    # step 1
    x1 = 1
    # next step
    while x1 < x:
        i1 += 1
        x1 += i1
    
    if x - x1 == 1:
        print(i1 + 1)
    else:
        print(i1)


tests = int(input())
for t in range(tests):
    solve()