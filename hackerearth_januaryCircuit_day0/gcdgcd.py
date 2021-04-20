from math import gcd

t = int(input())
while t>0:
    t-=1
    n = int(input())
    my_list = list(map(lambda x: x+1, range(n)))
    facto = my_list[0]
    for i in my_list[1:]:
        facto = facto*i//gcd(facto, i) 
    sums = sum(range(n+1))
    print(facto, sums)