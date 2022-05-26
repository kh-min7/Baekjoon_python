a = list(input())
stack = []

num = ['0','1','2','3','4','5','6','7','8','9']
oper = ['+', '-', '*' , '/']

for i in a:
  if i in num:
    stack.append(int(i))
  elif i in oper:
    y = stack.pop()
    x = stack.pop()

    if i == '+':
      stack.append(x + y)
    elif i == '-':
      stack.append(x - y)
    elif i == '*':
      stack.append(x * y)
    elif i == '/':
      stack.append(x / y)

print((stack.pop()))