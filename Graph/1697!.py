from collections import deque

n, k = map(int, input().split())

time = [0] * 100001


def bfs():
    queue = deque()
    queue.append(n)
    while queue:
        now = queue.popleft()
        if now == k:
            return
        for next in (now - 1, now + 1, now * 2):
            if 0 <= next <= 100000 and time[next] == 0:
                time[next] = time[now] + 1
                queue.append(next)

bfs()
print(time[k])