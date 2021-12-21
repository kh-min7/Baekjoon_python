from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

MAX = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] > MAX:
            MAX = graph[i][j]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y, h):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > h and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))


result = 1
for num in range(MAX):
    visited = [[0] * n for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(n):
            if graph[i][j] > num and visited[i][j] == 0:
                bfs(i, j, num)
                count += 1

    result = max(result, count)

print(result)
