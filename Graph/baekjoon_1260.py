from collections import deque

n, m, v = map(int, input().split())

matrix = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    matrix[a][b] = 1
    matrix[b][a] = 1

visit = [0] * (n + 1)

def dfs(start):
    visit[start] = 1
    print(start, end='')
    for i in range(1, n+1):
        if visit[i] == 0 and matrix[start][i] == 1:
            dfs(i)

def bfs(start):
    queue = deque()
    queue.append(start)
    visit[start] = 1
    while queue:
        start = queue.popleft()
        print(start, end='')
        for i in range(1, n+1):
            if visit[i] == 0 and matrix[start][i] == 1:
                visit[i] = 1
                queue.append(i)

dfs(v)
visit = [0] * (n + 1)
print()
bfs(v)

