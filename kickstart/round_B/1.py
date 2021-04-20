t = int(input())
for idx in range(t):
    N = input()
    S = input()
    result = ["1"]
    order = 1
    for i in range(len(S) - 1):
        if S[i + 1] > S[i]:
            order += 1
            result.append(str(order))
        else:
            order = 1
            result.append(str(order))
    
    print("Case #" + str(idx + 1) + ": "+ " ".join(result))