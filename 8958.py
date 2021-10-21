import sys

sys.stdin = open("input.txt", "r")

t = int(input())

for _ in range(t):
    a = list(input())
    cnt = 0
    sum = 0

    for x in a:
        if x == 'O':
            cnt += 1
            sum += cnt
        else:
            cnt = 0

    print(sum)
