num = int(input())
count = 0

while True:
    if (num % 5) == 0:
        count += num // 5
        print(count)
        break
    else:
        num = num - 3
        count += 1
        if num < 0:
            print("-1")
            break
