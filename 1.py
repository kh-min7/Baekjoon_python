a = list(input())
stack = []
result = []

operator_1 = ['+', '-']
operator_2 = ['*' , '/']

for i in a:
  if i == '(':
    stack.append(i)

  elif i == ')':
    while stack and stack[-1] != '(':
      result.append(stack.pop())
    stack.pop()
  
  elif i in operator_1:
    if not stack:
      stack.append(i)
    else:
      while stack and stack[-1] in operator_1 + operator_2:
        result.append(stack.pop())
      stack.append(i)
  
  elif i in operator_2:
    if not stack:
      stack.append(i)
    else:
      while stack and stack[-1] in operator_2:
        result.append(stack.pop())
      stack.append(i)
    
  else:
    result.append(i)

while stack:
  result.append(stack.pop())

print(''.join(result))