import sys
input = sys.stdin.readline

n = list(input().rstrip())
m = int(input().rstrip())

st = []

for _ in range(m):
  command = list(input().split())
  if command[0] == 'L':
    if n:
      st.append(n.pop())
  
  elif command[0] == 'D':
    if st:
      n.append(st.pop())
    
  elif command[0] == 'B':
    if n:
      n.pop()

  else:
    n.append(command[1])

n.extend(reversed(st))

print("".join(n))
