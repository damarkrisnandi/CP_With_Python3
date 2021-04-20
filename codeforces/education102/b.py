def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

t = int(input())
while t>0:
    t-=1
    s1 = input()
    s2 = input()
    l = compute_lcm(len(s1), len(s2))
    
    ans1 = s1*int(l/len(s1))
    ans2 = s2*int(l/len(s2))
    
    if ans1 == ans2:
        print(ans1)
    else:
        print(-1)