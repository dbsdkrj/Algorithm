from collections import deque
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)
n, m = map(int, input().split())
line = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    line[u].append(v)
    line[v].append(u)

visited = [0] * (n + 1)
result = []
cnt = 0


def bfs(s):
    global cnt
    q = deque()
    q.append(s)
    while q:
        a = q.popleft()
        for i in line[a]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)
    cnt += 1


bfs(1)
for i in range(2, n + 1):
    if visited[i] == 0:
        bfs(i)
print(cnt)