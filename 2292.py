N = int(input())

num = 1
ans = 1

for i in range(1, N):

    if N > num:
        num = num + 6 * i
        ans += 1

    else:
        break

print(ans)
