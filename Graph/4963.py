from collections import deque

dx = [0, 0, -1, 1, -1, -1, 1, 1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    maps[x][y] = 0

    while queue:
        x,y = queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<h and 0<=ny<w and maps[nx][ny] == 1:
                maps[nx][ny] = 0
                queue.append((nx,ny))



while True:

    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    maps = []
    for _ in range(h):
        maps.append(list(map(int, input().split())))

    cnt = 0
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1:
                cnt += 1
                bfs(i,j)

    print(cnt)



