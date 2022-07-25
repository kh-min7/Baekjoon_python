n, m = map(int, input().split())

s = {input() for _ in range(n)}
cnt = 0
lst = []

for i in range(m):
  a = input()
  if a in s:
    cnt += 1
    lst.append(a)

print(cnt)
lst.sort()
for x in lst:
  print(x)