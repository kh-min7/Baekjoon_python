import sys

sys.stdin = open("input.txt", "r")


height = []
for _ in range(9):
    height.append(int(input()))

sum_height = sum(height)

for i in range(len(height)):
    for j in range(i+1, len(height)):
        a, b = height[i], height[j]
        if sum_height - a - b == 100:
            height.remove(a)
            height.remove(b)
            break

height.sort()

for x in height:
    print(x)