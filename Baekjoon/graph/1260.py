import sys
input = sys.stdin.readline
from collections import deque

n,m,v = map(int, input().split())
line = [[] for _ in range(n+1)]

for _ in range(m):
    u, b = map(int, input().split())
    line[u].append(b)
    line[b].append(u)

for i in line:
    i.sort()
# [ [none], [2,3,4], [1,4], [1,4], [1,2,3] ]

d_cnt = 1
d_visited = [0] * (n+1)

def dfs(v):
    d_visited[v] = True
    print(v, end=" ")

    for k in line[v]:
        if d_visited[k] == 0:
            dfs(k)

def bfs(v):
    visited = [0] *(n+1)
    visited[v] = True
    q = deque([v])
    while q:
        a = q.popleft()
        print(a, end=" ")

        for k in line[a]:
            if visited[k] == 0:
                visited[k] = True
                q.append(k)

dfs(v)
print()
bfs(v)
