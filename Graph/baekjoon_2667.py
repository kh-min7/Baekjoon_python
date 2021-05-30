n = int(input())
graph = []
danji = []
count = 0
for _ in range(n):
    graph.append(list(map(int, input().strip())))


def dfs(x, y):
    global count
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    if graph[x][y] == 1:
        count += 1
        graph[x][y] = 0

        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True

    return False


for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            danji.append(count)
            count = 0

print(len(danji))
danji.sort()
for i in danji:
    print(i)