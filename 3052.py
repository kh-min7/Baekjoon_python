import sys

sys.stdin = open("input.txt", "r")

a = []
cnt = 0

for i in range(10):
    num = int(input()) % 42
    if num not in a:
        a.append(num)
        cnt += 1

print(cnt)