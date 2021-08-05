from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    cnt = 0

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                cnt += 1
    return cnt -1

computer = int(input())
network = int(input())

virus_map = [[0 for _ in range(computer+1)] for _ in range(computer+1)]

for _ in range(network):
    x, y = map(int, input().split())
    # 양방향 리스트
    virus_map[x].append(y)
    virus_map[y].append(x)

visited = [False] * len(virus_map)

print(bfs(virus_map, 1, visited))
