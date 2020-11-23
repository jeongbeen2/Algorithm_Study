num = int(input())

five = num // 5
three = (num % 5) // 3
eno = (num % 5) % 3

if eno == 0:
    print(five + three)

elif eno != 0:
    if num % 3 == 0:
        print(num // 3)

    elif num % 3 != 0:
        for i in range(1, five):
            num = num - 5 * i
        if (num % 3) == 0:
            print(i + (num // 3))
        else:
            print("-1")