import sys

sys.stdin = open("input.txt", "r")

num = int(input())
level = 1

while num > level:
    num -= level
    level += 1

if level % 2 == 0:
    x = num
    y = level - num + 1
else:
    x = level - num + 1
    y = num

print(f"{x}/{y}")
