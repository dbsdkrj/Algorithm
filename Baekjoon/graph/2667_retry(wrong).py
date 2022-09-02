#dfs = for문으로 재귀
#bfs = deque 써서 while q
import sys
sys.setrecursionlimit(5000)
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [list(map(int, str(input().rstrip()))) for _ in range(n)] #지도가 있는 이중리스트

dx = [0,0,-1,1]
dy = [-1,1,0,0]
#1을 찾고, 1과 연결된 칸을 모두 찾은다음 result 리스트에 넣기
result = []
#인수로 입력된 좌표와 붙은 1 찾기
def bfs(x,y):
    q=deque()
    q.append((x,y))
    global cnt
    while q:
        xx,yy = q.popleft()
        for i in range(4):
            nx = xx+dx[i]
            ny = yy+dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue

            if graph[nx][ny]==1:
                graph[nx][ny]=0
                q.append((nx,ny))
                cnt+=1

#지도에서 1을 찾기
for x in range(n):
    for y in range(n):
        if graph[x][y]==1:
            cnt=0
            bfs(x,y)
            result.append(cnt)
result.sort()
print(len(result))
for i in result:
    print(i)