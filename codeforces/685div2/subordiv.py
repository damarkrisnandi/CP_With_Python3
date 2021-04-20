def isPrime(num) : 
    if num > 1:
        for i in range(2,int(num)):
            if (int(num) % i) == 0:
                return False
        else:
            return True
    else:
        return False

def getLargestDivisor(num):
    largest = 1

    #2
    for i in range(2, num):
        #3
        if num % i == 0:
            #4
            largest = i 
    return largest

tests = int(input())
for t in range(tests):
    num = int(input())
    step = 0
    if num > 1:
        if num == 2:
            step = 1
        elif num == 3:
            step = 2
        elif num % 2 == 0:
            step = 2
        elif num % 2 != 0:
            step = 3  
    else:
        step  = 0

    print(step)