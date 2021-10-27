import sys

sys.stdin = open("input.txt", "r")

s = input()

a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in a:
    s = s.replace(i, '*')

print(len(s))

