import sys

sys.stdin = open("input.txt", "r")

s = input()

number = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

result = 0

for x in s:
    for y in number:
        if x in y:
            result += number.index(y) + 3

print(result)
