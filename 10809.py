import sys

sys.stdin = open("input.txt", "r")

s = input()

abc = 'abcdefghijklmnopqrstuvwxyz'

for i in abc:
    print(s.find(i), end=' ')