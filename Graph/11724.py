import sys
sys.setrecursionlimit(10000)

n,m = map(int, input().split())

matrix = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    u,v = map(int, input().split())
    matrix[u][v] = matrix[v][u] = 1

visit = [0] * (n+1)

def dfs(start):
    visit[start] = 1

    for i in range(1, n+1):
        if visit[i] == 0 and matrix[start][i] == 1:
            dfs(i)

cnt = 0

for i in range(1, n+1):
    if visit[i] == 0:
        dfs(i)
        cnt += 1

print(cnt)
