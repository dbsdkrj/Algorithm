from collections import deque

n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, input())))
# maze = [list(map(int, input())) for _ in range(n)]
'''
[ 0 1 2 3 4 ...m ]
[ 0 1 2 3 4 ...m ]
[ 0 1 2 3 4 ...m ]
n x m => n행 m열 => m개짜리 원소 n줄
가로 크기 m 세로크기 n

[ 0 1 2 3 4 ...m ], [ 0 1 2 3 4 ...m ], 
행렬은. 첫번째 인덱스가 행번호. 두번째가 열
maze[0][2]는 첫번째 행의 3번째 인덱스.
(x,y) = (0,0) => maze[0][0] = 첫번째줄 첫번째 
(1, 0) => maze[1][0] = 두번째줄 첫번째
(0, 1) => maze[0][1] = 첫번째줄 두번째
원래 아는 2차원 xy좌표로 생각하지말고 행렬로 생각하기
앞 인덱스가 y축 이동 (행번호니까!)
뒤 인덱스가 x축 이동 (열번호니까!)

그렇다면 앞 인덱스의 범위는? 0~n-1
뒤 인덱스의 범위는? 0~m-1
maze[nx][ny]에서 nx의 범위는? 0~n-1, ny의 범위는? 0~m-1

'''

dx = [-1,1,0,0]
dy = [0,0,-1,1] #1, -1, 0, 0

def bfs(graph, x, y):
    q = deque()
    q.append((x,y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m: #범위 제한.
                        #<-덕분에 [n-1][m-1]에서 더이상 진행 안함
                continue
            if graph[nx][ny]==1:
                graph[nx][ny] = graph[x][y] +1
                q.append((nx,ny))
    return graph[n-1][m-1]

print(bfs(maze, 0,0))

