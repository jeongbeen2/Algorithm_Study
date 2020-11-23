import sys

n = int(sys.stdin.readline())  # input() = sys.stdin.readline()
m = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    m.append(a+b)
for j in range(n):
    print(m[j])
