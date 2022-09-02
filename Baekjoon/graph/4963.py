# dfs가 for문으로 재귀
# bfs가 while문. deque 사용
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)
# graph[dy][dx]  --> [세로][가로]
dx = [0, 0, -1, 1, -1, 1, -1, 1]  # 가로
dy = [-1, 1, 0, 0, 1, 1, -1, -1]  # 세로


# 위, 아래,오른쪽, 왼쪾. 오른쪽위 오른쪾아래 왼쪽 위 왼쪽 아래

def bfs(mp, x, y):  # 붙어있는 1 == 섬의 개수 세기
    mp[x][y] = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        # nx는 0부터 w-1까지
        if nx < 0 or nx >= h or ny < 0 or ny >= w:
            continue
        if mp[nx][ny] == 1:
            bfs(mp, nx, ny)


while 1:
    w, h = map(int, input().split())  # y x
    if w == 0 and h == 0:
        break

    mp = []
    for i in range(h):
        mp.append(list(map(int, input().split())))
    cnt = 0
    # 1이 있는 곳을 찾아야됨 2차원이니까 2중 for문
    for x in range(h):
        for y in range(w):
            if mp[x][y] == 1:
                bfs(mp, x, y)
                cnt += 1
    print(cnt)
