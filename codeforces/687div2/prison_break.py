def inputArray():
    return list(map(int,input().strip().split()))
  
def solve():
    n,m,r,c = inputArray()
    print(max((abs(r - 1) + abs(c - 1)), (abs(r - n) + abs(c - m)), (abs(r - n) + abs(c - 1)), (abs(r - 1) + abs(c - m))))

tests = int(input())
for t in range(tests):
    solve()