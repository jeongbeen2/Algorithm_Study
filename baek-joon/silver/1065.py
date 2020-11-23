inputNum = int(input())
hansu = 0  # hansu <= 1000

for n in range(1, inputNum+1):
    if n <= 99:
        hansu += 1

    elif n <= 1000:
        bigNum = list(map(int, str(n)))
        if (bigNum[0] + bigNum[2]) / 2 == bigNum[1]:
            hansu += 1
    else:
        print("your input num over 1000")
        exit()
print(hansu)
