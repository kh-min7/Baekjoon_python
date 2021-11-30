import sys

sys.stdin = open("input.txt", "r")

t = int(input())

fi_0 = [1, 0, 1]
fi_1 = [0, 1, 1]


def fibo(x):
    a_len = len(fi_0)
    if a_len <= x:
        for i in range(a_len, x + 1):
            fi_0.append(fi_0[i - 2] + fi_0[i - 1])
            fi_1.append(fi_1[i - 2] + fi_1[i - 1])
    return fi_0[x], fi_1[x]


for _ in range(t):
    n = int(input())
    x, y = fibo(n)
    print(x, y)
