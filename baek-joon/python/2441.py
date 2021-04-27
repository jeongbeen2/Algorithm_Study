n = int(input())
m = n
for i in range(n):
    print(" " * (n - m) + "*" * m)
    m -= 1