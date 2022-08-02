from collections import deque

m, n, h = map(int, input().split())
tomato = [[list(map(int, input().split())) for i in range(n)]for j in range(h)]
q = deque()

dz = [-1,1,0,0,0,0] #층
dx = [0,0,-1,1,0,0] #행
dy = [0,0,0,0,-1,1] #열
# n x m 행렬이 h개 쌓여있음
# m개짜리 줄 n개가 h개
# tomato[h선택][n선택][m선택]
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k]==1:
                q.append([i,j,k])

def bfs():
    while q:
        z,x,y = q.popleft()
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if nz<0 or nz>=h or nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if tomato[nz][nx][ny]==0:
                tomato[nz][nx][ny]=tomato[z][x][y]+1
                q.append([nz,nx,ny])
bfs()
day = 0
for i in tomato:
    for j in i:
        for k in j:
            if k ==0:
                print(-1)
                exit(0)
            day = max(day,k)
print(day-1)