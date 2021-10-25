import sys

sys.stdin = open("input.txt", "r")

n = int(input())

a = list(map(int, input().split()))

print(min(a), max(a))