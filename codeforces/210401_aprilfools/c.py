ini = []
for i in input():
    ini.append((ord(i) + 1) % 2)

val = True
for i in range(2,len(ini)):
    if ini[i] != ini[i-1]^ini[i-2]:
        val = False
        break

if val:
    print("YES")
else:
    print("NO")