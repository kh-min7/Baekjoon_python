import sys

sys.stdin = open("input.txt", "r")

s = input().split("-")

for i in range(len(s)):
    print(s[i][0], end="")