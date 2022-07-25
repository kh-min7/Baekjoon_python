n, m = map(int, input().split())

a = set(map(int, input().split()))
b = set(map(int, input().split()))

cnt_a = 0
cnt_b = 0
for x in a:
  if x not in b:
    cnt_a += 1

for y in b:
  if y not in a:
    cnt_b += 1

print(cnt_a + cnt_b)