import sys

sys.stdin = open("input.txt", "r")

while True:

    a = [0] * 4

    try:
        n = input()

        for i in range(len(n)):
            if n[i] >= 'a' and n[i] <= 'z':
                a[0] += 1
            elif n[i] >= 'A' and n[i] <= 'Z':
                a[1] += 1
            elif n[i] >= '0' and n[i] <= '9':
                a[2] += 1
            elif n[i] == " ":
                a[3] += 1

        print(a[0], a[1], a[2], a[3])

    except:
        break
