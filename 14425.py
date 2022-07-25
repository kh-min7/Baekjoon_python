n, m = map(int, input().split())

S = {input() for _ in range(n)}

cnt = 0

for i in range(m):
  if input() in S:
    cnt += 1

print(cnt)