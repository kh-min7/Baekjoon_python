import sys

sys.stdin = open("input.txt", "r")

x = []
y = []

for i in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

if x[0] == x[1]:
    ans_x = x[2]
elif x[1] == x[2]:
    ans_x = x[0]
elif x[2] == x[0]:
    ans_x = x[1]

if y[0] == y[1]:
    ans_y = y[2]
elif y[1] == y[2]:
    ans_y = y[0]
elif y[2] == y[0]:
    ans_y = y[1]

print(ans_x, ans_y)