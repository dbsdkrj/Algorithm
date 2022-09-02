import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)
from collections import deque

m, n = map(int, input().split())  # x, y
tomato = [list(map(int, input().rstrip().split())) for i in range(n)]
q = deque()
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs():  # 1의 좌표

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] + 1
                q.append((nx, ny))


# 익은토마토(1) 위치 찾기  --
for x in range(n):
    for y in range(m):
        if tomato[x][y] == 1:
            q.append((x, y))  # --> 동시에 찾는법 == q에 append하고 bfs 실행
            # dfs는 불가(popleft()불가. )
bfs()
ma = 0

for x in tomato:
    for y in x:
        if y == 0:  # tomato에 0이 있으면 다 안익음
            print(-1)
            exit(0)

    ma = max(ma, max(x))
print(ma - 1)


