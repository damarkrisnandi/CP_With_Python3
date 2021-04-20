print(1337 // 69)
t = int(input())
while t>0:
    t-=1
    n, k = list(map(int, input().split(" ")))
    A = list(range(n + 1))
    A.remove(0)
    A.sort(reverse=True)
    print(A)
    # B = list(range(n + 1))
    # B.remove(0)
    B = []
    for i in range(len(A)):
        print(len(B))
        if A[i] == i+1:
            B.append(A[i-1])
        else:
            if len(B) == 0:
                B.append(i+1)
            else:
                if i+1 == B[i-1] and i+2 <= len(A):
                    B.append(i+2)
                else:
                    B.append(A[i-1])
    
    print(B[k-1])