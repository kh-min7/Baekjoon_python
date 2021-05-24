coins = [500, 100, 50, 10, 5, 1]

money = int(input())
price = 1000 - money

answer = 0

for i in range(len(coins)):
	if price >= coins[i]:
		answer += price // coins[i]
		price %= coins[i]

print(answer) 
