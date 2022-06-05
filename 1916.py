import heapq
import sys

input = sys.stdin.readline
INF = float("INF")

N = int(input())
M = int(input())

heap = []
dp = [INF] * (N + 1)

graph = [[] for _ in range(N + 1)]
for _ in range(M):
  start, cost, end = map(int, input().split())
  graph[start].append((end, cost))

start_num, end_num = map(int, input().split())

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

Dijkstra(start_num)

print(dp[end_num])