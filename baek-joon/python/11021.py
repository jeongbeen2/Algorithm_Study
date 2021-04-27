n = int(input())
i = 1
c = []
while i <= n:
    a, b = map(int, input().split(" "))
    c.append(a + b)
    if i == n:
        for j in range(len(c)):
            print(f"Case #{j+1}: {c[j]}")
    i += 1
