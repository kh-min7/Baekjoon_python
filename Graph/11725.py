from collections import deque

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0] * (n + 1)


def bfs():
    queue = deque()
    queue.append(1)
    visited[0] = 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                visited[i] = v
                queue.append(i)
bfs()
for i in range(n - 1):
    print(visited[i + 2])