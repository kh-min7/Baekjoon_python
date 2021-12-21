from collections import deque


def bfs():
    m, n, h = map(int, input().split())
    graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dh = [0, 0, 0, 0, 1, -1]

    queue = deque()

    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 1:
                    queue.append((i, j, k, 0))

    d = 0
    while queue:
        z, x, y, d = queue.popleft()
        for i in range(6):
            nh = z + dh[i]
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nh < h and 0 <= nx < n and 0 <= ny < m and graph[nh][nx][ny] == 0:
                graph[nh][nx][ny] = 1
                queue.append((nh, nx, ny, d + 1))

    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 0:
                    return -1

    return d

print(bfs())