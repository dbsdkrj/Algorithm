from collections import deque


def bfs(graph, x, y):
    dx = [-1, 1, 0, 0]  # 좌 우
    dy = [0, 0, -1, 1]  # 상 하
    cnt = 1
    q = deque()
    q.append((x, y))
    graph[y][x] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                cnt += 1
                q.append((nx, ny))
    return cnt


t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())  # x 범위, y범위
    farm = [[0 for _ in range(m)] for j in range(n)]

    for i in range(k):
        u, v = map(int, input().split())
        farm[v][u] = 1
        # print(farm)

    count = [bfs(farm, i, j) for i in range(m) for j in range(n) if farm[j][i] == 1]
    print(len(count))
