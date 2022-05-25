a = list(input())

stack = []
result = 0
tmp = 1

for i in range(len(a)):
    if a[i] == '(':
        stack.append(a[i])
        tmp *= 2

    elif a[i] == '[':
        stack.append(a[i])
        tmp *= 3

    elif a[i] == ')':
        if not stack or stack[-1] == '[':
            result = 0
            break
        if a[i-1] == '(':
            result += tmp
        stack.pop()
        tmp //= 2

    else:
        if not stack or stack[-1] == '(':
            result = 0
            break
        if a[i-1] == '[':
            result += tmp
        stack.pop()
        tmp //= 3
        
if stack:
    print(0)
else:
    print(result)
