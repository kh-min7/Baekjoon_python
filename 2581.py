import sys

sys.stdin = open("input.txt", "r")

m = int(input())
n = int(input())


def primeNum(x):
    cnt = 0

    if x <= 1:
        cnt = 0

    elif x == 2:
        cnt = 1

    else:
        for i in range(2, x):
            if x % i == 0:
                cnt = 0
                break
            else:
                cnt = 1

    return cnt


nums = []

for i in range(m, n + 1):
    if primeNum(i) == 1:
        nums.append(i)

if len(nums) > 0:
    print(sum(nums))
    print(min(nums))
else:
    print(-1)