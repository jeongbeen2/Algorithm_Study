A = int(input())
B = int(input())
C = int(input())

num_list = list(map(int, str(A * B * C)))

for i in range(0, 10):
    num_count = num_list.count(i)
    print(num_count)