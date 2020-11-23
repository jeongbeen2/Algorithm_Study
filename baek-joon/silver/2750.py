n = int(input())
my_list = []
for i in range(n):
    m = int(input())
    my_list.append(m)
    my_list.sort()

for j in my_list:
    print(j)