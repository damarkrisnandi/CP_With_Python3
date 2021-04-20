import math
def isPrime(num) : 
    if num > 1:
        for i in range(2,int(num)):
            if (int(num) % i) == 0:
                return False
        else:
            return True
    else:
        return False

t = int(input())
for idx in range(t):
    n = int(input())
    root = int(math.floor(math.sqrt(n)))
    root2 = root
    while (isPrime(root) == False):
        root -= 1
    while (isPrime(root2) == False or root2 == root):
        root2 += 1

    if root * root2 > n:
        root2 = root
        while (isPrime(root2) == False or root2 == root):
            root2 -= 1
    
    print("Case #" + str(idx + 1) + ": "+ str(root * root2))