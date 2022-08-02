from collections import deque

m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]
q = deque([])
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 익어있는 토마토 위치 일단 저장
# (q.append([i,j]) for i in range(n) for j in range(m) if tomato[i][j]==1)
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            q.append([i, j])

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if tomato[nx][ny]==0:
                tomato[nx][ny]=tomato[x][y]+1
                q.append([nx,ny])
bfs()
day=0
for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(day, max(i))
print(day - 1)