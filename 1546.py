import sys

sys.stdin = open("input.txt", "r")

n = int(input())

a = list(map(int, input().split()))

m = max(a)

for i in range(n):
    a[i] = a[i] / m * 100

sum = 0
for x in a:
    sum += x

print(sum / n)