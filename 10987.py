import sys

sys.stdin = open("input.txt", "r")

n = input()

a = ['a', 'e', 'i', 'o', 'u']

cnt = 0

for i in n:
    if i in a:
        cnt += 1

print(cnt)