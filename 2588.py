import sys

sys.stdin = open("input.txt", "r")

a = int(input())
b = input()

for i in range(len(b)):
    print(a * int(b[-i-1]))

print(a * int(b))