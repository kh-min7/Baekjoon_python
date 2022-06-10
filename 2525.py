a, b = map(int, input().split())
c = int(input())

def clock(a, b, c):
  b += c
  if b >= 60:
    d = b // 60
    e = b % 60
  
    b = e
    a += d

  if a >= 24:
    a -= 24
  
  print(a, b)

clock(a, b, c)