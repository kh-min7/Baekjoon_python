
n = int(input())

a = n
cnt = 0

while True:
    ten = a // 10
    one = a % 10
    sum = ten + one
    cnt += 1
    a = int(a % 10) * 10 + int(sum % 10)
    if (a == n):
        break

print(cnt)