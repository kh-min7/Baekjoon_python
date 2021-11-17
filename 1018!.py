import sys

sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())

a = [(input()) for _ in range(N)]

cnt = []

for n in range(N-7):
    for m in range(M-7):
        first_W = 0
        first_B = 0

        for i in range(n, n+8):
            for j in range(m, m+8):
                if (i+j) % 2 == 0:
                    if a[i][j] != 'W':
                        first_W += 1
                    if a[i][j] != 'B':
                        first_B += 1
                else:
                    if a[i][j] != 'B':
                        first_W += 1
                    if a[i][j] != 'W':
                        first_B += 1
        cnt.append(first_W)
        cnt.append(first_B)

print(min(cnt))