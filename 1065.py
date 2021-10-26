import sys

sys.stdin = open("input.txt", "r")

n = int(input())
sum = 0

for i in range(1, n + 1):
    if i < 100:
        sum += 1
    else:
        n_str = list(map(int, str(i)))
        if n_str[2] - n_str[1] == n_str[1] - n_str[0]:
            sum += 1

print(sum)
