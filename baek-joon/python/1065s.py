print(sum(i < 100 or i//10 % 10*2 == i %
          10+i//100 for i in range(1, int(input())+1)))
