from collections import deque

def bfs():
    m, n, h = map(int, input().split())
    graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

