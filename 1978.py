import sys

sys.stdin = open("input.txt", "r")

n = int(input())
nums = list(map(int, input().split()))

for num in nums:
    if num <= 1:
        n -= 1

    for i in range(2, num):
        if num % i == 0:
            n -= 1
            break

print(n)