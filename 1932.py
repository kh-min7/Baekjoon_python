n = int(input())
dp = []
for _ in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i + 1):
        # 대각선 왼쪽
        if j == 0: left = 0
        else: left = dp[i - 1][j - 1]

        # 대각선 오른쪽
        if j == i: right = 0
        else: right = dp[i - 1][j]

        dp[i][j] = dp[i][j]+max(left, right)

result = 0
for i in range(n):
    result = max(result, dp[n-1][i])

print(result)
