N, K = map(int, input().split())
N_list = []
answer = 0

for _ in range(N):
	temp = int(input())
	N_list.append(temp)

for i in range(N-1, -1, -1):
	if K >= N_list[i]:
		answer += K // N_list[i]
		K %= N_list[i]

print(answer)

