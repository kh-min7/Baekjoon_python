import sys

sys.stdin = open("input.txt", "r")

n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

left = 1
right = 1

left_max = a[0]
right_max = a[-1]

for i in range(1, n):
    if a[i-1] < a[i] and left_max < a[i]:
        left_max = a[i]
        left += 1

for i in range(0, n-1):
    if a[n-i-1] < a[n-i-2] and right_max < a[n-i-2]:
        right_max = a[n-i-2]
        right += 1

print(left)
print(right)

