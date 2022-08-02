from collections import deque
'''
행 -2, 열 -1
행 -1, 열 -2
행 -2, 열 +1
행 -1, 열 +2

행 +2, 열 -1
행 +1, 열 -2
행 +2, 열 +1
행 +1, 열 +2
'''
dx=[-2,-1,-2,-1,2,1,2,1]
dy=[-1,-2,1,2,-1,-2,1,2]

def bfs(chess, sx,sy,ex,ey):
    q = deque()
    q.append([sx,sy])
    chess[sx][sy] = 1 #시작위치를 1
    while q:
        x, y = q.popleft()
        if x == ex and y == ey: #이 위치가 목적지면
            print(chess[ex][ey]-1)
            return
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if chess[nx][ny]==0:
                q.append([nx,ny])
                chess[nx][ny] = chess[x][y] +1

t = int(input())

for _ in range(t):
    n = int(input())
    chess = [[0]*n for i in range(n)]
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    bfs(chess, sx, sy, ex, ey)