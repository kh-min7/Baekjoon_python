import copy

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

max_val = 0


def wall(start, count):
    global max_val

    if count != 3:
        for i in range(start, n * m):
            x = i // m
            y = i % m

            if graph[x][y] == 0:
                graph[x][y] = 1
                wall(i, count + 1)
                graph[x][y] = 0

    else:
        select_ver = copy.deepcopy(graph)
        for x in range(n):
            for y in range(m):
                virus(x, y, select_ver)
        safe_zone = sum(i.count(0) for i in select_ver)
        max_val = max(max_val, safe_zone)
        return True


def virus(x, y, select_ver):
    if select_ver[x][y] == 2:

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if select_ver[nx][ny] == 0:
                    select_ver[nx][ny] = 2
                    virus(nx, ny, select_ver)


wall(0, 0)
print(max_val)
