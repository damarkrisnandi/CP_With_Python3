import time

def solve(arr):
    for i in arr:
        print(i)

def join_newline(arr):
    print("\n".join(a))

a = ["a", "b", "c", "a", "b", "c", "a", "b", "c", "a", "b", "c", "a", "b", "c", "a", "b", "c",
"a", "b", "c", "a", "b", "c", "a", "b", "c", "a", "b", "c", "a", "b", "c", "a", "b", "c",
"a", "b", "c", "a", "b", "c", "a", "b", "c", "a", "b", "c", "a", "b", "c", "a", "b", "c"]
start_time = time.time()
solve(a)
exec_loop = time.time() - start_time


start_time = time.time()
join_newline(a)
exec_join_nl = time.time() - start_time

print("--- loop: %s seconds ---" % (exec_loop))
print("--- join newline: %s seconds ---" % (exec_join_nl))
    