a, b, c = map(int, input().split())

if a == b == c:
  ans = 10000 + a * 1000
  print(ans)
elif a == b and b != c:
  ans = 1000 + a * 100
  print(ans)
elif b == c and a != b:
  ans = 1000 + b * 100
  print(ans)
elif c == a and a != b:
  ans = 1000 + a * 100
  print(ans)
else:
  ans = max(a, b, c) * 100
  print(ans)