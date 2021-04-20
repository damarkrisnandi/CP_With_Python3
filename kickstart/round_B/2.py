t = int(input())
for idx in range(t):
    l = input()
    A = list(map(int, input().split(" ")))
    result = 0
    A_diff = []
    for i in range(len(A) - 1):
        A_diff.append(A[i + 1] - A[i])
    
    if len(set(A_diff)) == 1:
        result = len(A)
    print(A_diff)
    print("Case #" + str(idx + 1) + ": "+ str(result))