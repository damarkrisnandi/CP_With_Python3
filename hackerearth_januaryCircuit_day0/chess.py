t = int(input())
while t>0:
    t-=1
    [x1, y1] = list(map(int, input().split()))
    [x2, y2] = list(map(int, input().split()))
 
    lost_second = [[1, 1], [1, 8], [8, 1], [8, 8]]
    if (abs(x1 - x2) == 1 or abs(y1 - y2) == 1):
        print("FIRST")
    elif (x1 == x2 and y1 == y2):
        print("SECOND")
    else:
        print("DRAW")