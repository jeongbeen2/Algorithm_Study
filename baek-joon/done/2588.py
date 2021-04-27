n1, n2 = int(input()), int(input())
n3, n4, n5, n6 = (
    n1 * (n2 % 10),
    n1 * ((n2 % 100 - n2 % 10) // 10),
    n1 * (n2 // 100),
    n1 * n2,
)
print(n3)
print(n4)
print(n5)
print(n6)