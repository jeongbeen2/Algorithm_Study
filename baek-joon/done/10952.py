num_list = []
while True:
    n1, n2 = map(int, input().split(" "))
    num_list.append(n1 + n2)
    if n1 + n2 <= 1:
        for j in range(len(num_list) - 1):
            print(num_list[j])
        break