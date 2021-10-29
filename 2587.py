import sys

sys.stdin = open("input.txt", "r")

a = []
sum = 0

for i in range(5):
    a.append(int(input()))
    sum += a[i]

a.sort()

print(sum // 5)
print(a[5//2])