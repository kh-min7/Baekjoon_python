from collections import deque

t = int(input())

for _ in range(t):
    i = int(input())
    graph = [[-1] * i for _ in range(i)]
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [-2, -1, 1, 2, -2, -1, 1, 2]

    if start_x == end_x and start_y == end_y:
        print(0)

    else:
        queue = deque()
        queue.append((start_x, start_y))
        graph[start_x][start_y] = 0
        while queue:
            x, y = queue.popleft()
            for j in range(8):
                nx = x + dx[j]
                ny = y + dy[j]

                if 0 <= nx < i and 0 <= ny < i and graph[nx][ny] == -1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))

        print(graph[end_x][end_y])
