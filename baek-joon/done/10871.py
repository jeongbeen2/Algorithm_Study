n, x = map(int, input().split())
a = list(map(int, input().split()))
new_a = []
for i in range(n):
    if a[i] < x:
        new_a.append(a[i])

print(*new_a)
