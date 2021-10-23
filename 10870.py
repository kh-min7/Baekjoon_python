import sys

sys.stdin = open("input.txt", "r")

n = int(input())


def fibo(x):
    if x <= 1:
        return x

    return fibo(x - 2) + fibo(x - 1)


print(fibo(n))
