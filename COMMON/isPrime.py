def isPrime(num) : 
    if num > 1:
        for i in range(2,int(num)):
            if (int(num) % i) == 0:
                return False
        else:
            return True
    else:
        return False