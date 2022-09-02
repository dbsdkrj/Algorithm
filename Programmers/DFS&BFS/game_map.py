from collections import deque
import sys

sys.setrecursionlimit(1000)
input = sys.stdin.readline


def bfs(maps, x, y):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    # 경로 지날때마다 1 증가시키기
    n = len(maps[0])  # y
    m = len(maps)  # x
    q = deque()
    q.append((x, y))
    while q:
        xx, yy = q.popleft()
        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[xx][yy] + 1
                q.append((nx, ny))


def solution(maps):
    n = len(maps[0])  # y
    m = len(maps)  # x
    # (0,0)부터 출발해서 1의 위치 따라가기

    bfs(maps, 0, 0)

    if maps[m - 1][n - 1] > 1:
        return (maps[m - 1][n - 1])
    else:
        return -1
# dfs 함수 따로쓰면 x?
# 결과를 print 말고 return


# def solution(maps):
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#     n = len(maps)
#     m = len(maps[0])
#
#     queue = deque()
#     queue.append((0, 0))
#
#     while queue:
#         x, y = queue.popleft()
#
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if nx >= 0 and nx < n and ny >= 0 and ny < m:
#                 if maps[nx][ny] == 1:
#                     maps[nx][ny] = maps[x][y] + 1
#                     queue.append((nx, ny))
#     if maps[n - 1][m - 1] > 1:
#         return maps[n - 1][m - 1]
#     else:
#         return -1
