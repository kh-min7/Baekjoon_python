n = int(input())
array = [0] * 301
for i in range(1, n + 1):
    array[i] = int(input())

dp = [0] * 301

dp[1] = array[1]
dp[2] = array[1] + array[2]
dp[3] = max(array[1], array[2]) + array[3]

for i in range(4, n + 1):
    dp[i] = max(dp[i - 2], dp[i - 3] + array[i - 1]) + array[i]

print(dp[n])
