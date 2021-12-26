from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0] * (n + 1)


def bfs(start):
    queue = deque()
    queue.append(start)
    visited[a] = 1
    while queue:
        q = queue.popleft()
        for i in graph[q]:
            if i == b:
                return visited[q]
            if not visited[i]:
                visited[i] = visited[q] + 1
                queue.append(i)
    return -1


print(bfs(a))
