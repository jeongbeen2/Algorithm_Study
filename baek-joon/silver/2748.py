n, memo = int(input()), {0: 0, 1: 1}


def fib(n, memo):
    if n in memo:
        return memo[n]
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


print(fib(n, memo))
