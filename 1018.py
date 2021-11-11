import sys

sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())

a = []

for _ in range(n):
    a.append(input())

