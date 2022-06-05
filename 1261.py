import sys, heapq

INF = float("INF")

graph = []
m, n = map(int, input().split())
distance = [[INF] * m for _ in range(n)]

for _ in range(n):
  graph.append(list(map(int, input())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def Dijkstra():
  q = []
  distance[0][0] = 0
  heapq.heappush(q, (graph[0][0], 0, 0))

  while q:
    wall, x, y = heapq.heappop(q)
    if x == n - 1 and y == m - 1:
      print(distance[x][y])
      break

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < m:
        new_wall = wall + graph[nx][ny]
        if new_wall < distance[nx][ny]:
          distance[nx][ny] = new_wall
          heapq.heappush(q, (new_wall, nx, ny))

Dijkstra()
