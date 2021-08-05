n, m = map(int, input().split())
cards = list((map(int, input().split())))
ans = 0

for i in cards:
    for j in cards:
        if i == j:
            continue
        for k in cards:
            if i == k:
                continue
            if j == k:
                continue

            tmp = i + j + k

            if ans < tmp <= m:
                ans = tmp

print(ans)


