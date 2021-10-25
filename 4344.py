import sys

sys.stdin = open("input.txt", "r")

c = int(input())

for _ in range(c):
    sum = 0
    avg = 0
    cnt = 0

    n = list(map(int, input().split()))

    for i in range(1, len(n)):
        sum += n[i]

    avg = sum / n[0]

    for i in range(1, len(n)):
        if n[i] > avg:
            cnt += 1

    ans = (cnt / n[0] * 100)

    print(f"{ans:.3f}%")