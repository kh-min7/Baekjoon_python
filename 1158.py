from collections import deque

n, k = map(int, input().split())

dq = deque([i for i in range(1, n + 1)])
ans = []

while dq:
  dq.rotate(-k+1)
  ans.append(dq.popleft())



print("<", ", ".join(str(i) for i in ans), ">", sep="")
