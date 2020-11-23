num = int(input())
all_num = str(input())
result = 0

for i in range(num):
    result += int(all_num[i])
print(result)

# run time error
""" num = int(input())
all_num = list(map(int, str(int(input()))))
plus_all = 0

for i in range(num):
    plus_all += all_num[i]

print(plus_all) """
