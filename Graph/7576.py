from collections import deque

m, n = map(int, input().split())

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs():
    cnt = 0
    while ripen_tomato:
        cnt += 1
        for _ in range(len(ripen_tomato)):
            y, x = ripen_tomato.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<m and 0<=ny<n and tomato[ny][nx] == 0:
                    tomato[ny][nx] = 1
                    ripen_tomato.append([ny, nx])
    return cnt

tomato = []
for _ in range(n):
    tomato.append(list(map(int, input().split())))
ripen_tomato = deque()

for y in range(n):
    for x in range(m):
        if tomato[y][x] == 1:
            ripen_tomato.append([y,x])


ans = bfs() - 1

for y in range(n):
    for x in range(m):
        if tomato[y][x] == 0:
            print(-1)
            exit()

print(ans)