def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    graph[x][y] = 1
    result = 1

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and not graph[nx][ny]:
                result += 1
                graph[nx][ny] = 1
                queue.append((nx,ny))

    return result


from collections import deque

m, n, k = map(int, input().split())

graph = [[0]*n for i in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[j][i] = 1

cnt = 0
ans = []

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            cnt += 1
            ans.append(bfs(i,j))

print(cnt)
print(' '.join([str(i) for i in sorted(ans)]))

# 34~36줄 이해하기, 48줄 join 이해하기