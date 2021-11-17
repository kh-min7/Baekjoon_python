import sys

ipt = sys.stdin.readline

n = int(ipt())

count = [0] * 10001

for i in range(n):
    num = int(input())
    count[num] += 1

for i in range(10001):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)