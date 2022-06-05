import heapq

INF = float("INF")

n = int(input())
graph = []
for _ in range(n):
  graph.append(list(map(int, input())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visit = [[0] * n for _ in range(n)]

def Dijkstra():
  q = []
  visit[0][0] = 1
  heapq.heappush(q, (0, 0, 0))

  while q:
    cost, x, y = heapq.heappop(q)
    if x == n - 1 and y == n - 1:
      print(cost)
      break

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
        visit[nx][ny] = 1
        if graph[nx][ny] == 0:
          heapq.heappush(q, (cost + 1, nx, ny))
        else:
          heapq.heappush(q, (cost, nx, ny))

Dijkstra()