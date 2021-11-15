n = int(input())


def star(len):
    if len == 1:
        return ['*']

    stars = star(len // 3)
    a = []

    for s in stars:
        a.append(s * 3)
    for s in stars:
        a.append(s + ' ' * (len // 3) + s)
    for s in stars:
        a.append(s * 3)

    return a

print('\n'.join(star(n)))
