import sys

sys.stdin = open("input.txt", "r")

def isprime(num):
    sqr = int(num ** (1/2))

    if num == 1:
        return False

    for j in range(2, sqr + 1):
        if num % j == 0:
            return False
    return True

m, n = map(int, input().split())

for i in range(m, n + 1):
    if isprime(i):
        print(i)

3, 7
2, 3, 5
