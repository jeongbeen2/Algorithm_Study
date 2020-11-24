for _ in range(int(input())):
    t, s = 0, 0
    for i in input():
        if i == "O":
            s += 1
        else:
            s = 0
        t += s
    print(t)