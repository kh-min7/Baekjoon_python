import sys

sys.stdin = open("input.txt", "r")

x, y, w, h = list(map(int, input().split()))

fake_min = max(w, h)


y_min = min(y, abs(y-h))
x_min = min(x, abs(x-w))
total_min = min(x_min, y_min)

if total_min < fake_min:
    fake_min = total_min
    print(fake_min)