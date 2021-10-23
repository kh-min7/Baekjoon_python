import sys

sys.stdin = open("input.txt", "r")

s = input()

while len(s) > 10:
    print(s[0:10], end='\n')
    s = s[10:]

if len(s) < 10:
    print(s)
