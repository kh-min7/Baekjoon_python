count = 0

for i in range(8):
    chess = input()
    for j in range(8):
        if (i + j) % 2 == 0 and chess[j] == 'F':
            count += 1

print(count)