n = int(input())

for i in range(1, n + 1):
    print("*" * i + " " * ((n - i) * 2) + "*" * i)

for j in reversed(range(1, n)):
    print("*" * j + " " * ((n - j) * 2) + "*" * j)