n = int(input())
check = n
count = 0
result = 0
new_num = 0

while True:
    result = n//10 + n % 10
    new_num = (n % 10)*10 + result % 10
    n = new_num
    count += 1

    if n == check:
        print(count)
        break
