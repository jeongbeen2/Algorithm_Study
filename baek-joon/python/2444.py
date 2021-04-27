n = int(input())
m = 1
N = n - 1
for i in range(n - 1):
    print(" " * N + ("*" * (2 * m - 1)))
    m += 1
    N -= 1
x = n
N = 0
for i in range(n):
    print(" " * N + ("*" * (2 * x - 1)))
    x -= 1
    N += 1