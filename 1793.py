def tile(n):
    d[1] = 1
    d[2] = 3

    for i in range(3, n + 1):
        d[i] = 2 * d[i - 2] + d[i - 1]
    return d[n]


d = [0] * 251

while True:
    try:
        n = int(input())
        print(tile(n))

    except:
        break
