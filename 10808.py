import sys

sys.stdin = open("input.txt", "r")

s = input()

a = 'abcdefghijklmnopqrstuvwxyz'

a_list = [0] * len(a)

for x in s:
    for i in range(len(a)):
        if a[i] == x:
            a_list[i] += 1

for i in range(len(a_list)):
    print(a_list[i], end=' ')