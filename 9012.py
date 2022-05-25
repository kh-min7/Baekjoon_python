t = int(input())

for _ in range(t):
  a = list(input())
  stack = []

  for i in a:
    if i == '(':
      stack.append(i)
    elif i == ')':
      if stack:
        stack.pop()
      else:
        stack.append(i)
        break
    
  if len(stack) == 0:
    print("YES")
  else:
    print("NO")