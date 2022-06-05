import sys
import heapq

input = sys.stdin.readline
INF = float("INF")

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V + 1)] 
heap = []
dp = [INF] * (V + 1)

for _ in range(E):
  u, v, w = map(int, input().split())
  graph[u].append((w, v))

def Dijkstra(start):
  dp[start] = 0
  heapq.heappush(heap, (0, start))

  while heap:
    weight, now = heapq.heappop(heap)

    if dp[now] < weight:
      continue
    
    for w, next_node in graph[now]:
      next_weight = w + weight
      if next_weight < dp[next_node]:
        dp[next_node] = next_weight
        heapq.heappush(heap, (next_weight, next_node))

Dijkstra(K)

for i in dp[1:]:
  print(i if i != INF else "INF")