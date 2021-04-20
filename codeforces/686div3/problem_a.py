tests = int(input())
for t in range(tests):
    size = int(input())
    result = str(size) + " "
    for i in range(size - 1):
        result += str(i + 1) + " "
    print(result)