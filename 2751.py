import sys

sys.stdin = open("input.txt", "r")

ipt = sys.stdin.readline

n = int(ipt())
a = []
for _ in range(n):
    a.append(int(ipt()))

a.sort()

for i in a:
    print(i)