n = int(input())
m = n
N = 0
for i in range(n):
    print(" " * N + ("*" * (2 * m - 1)))
    m -= 1
    N += 1