import sys

sys.stdin = open("input.txt", "r")


def isprime(num):
    sqr = int(num ** (1 / 2))

    if num == 1:
        return False

    for j in range(2, sqr + 1):
        if num % j == 0:
            return False
    return True

a = []

while True:
    n = int(input())
    if n == 0:
        break
    cnt = 0

    for i in range(n + 1, 2 * n + 1):
            if isprime(i):
                cnt += 1

    a.append(cnt)

for i in a:
    print(i)
