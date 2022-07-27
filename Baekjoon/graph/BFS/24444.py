import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
from collections import deque

n, m, r = map(int, input().split())
link = [[] for _ in range(n + 1)]  # 간선[ [ ], [ ], [ ], [ ], [ ] ]

# 양방향 간선
for _ in range(m):
    u, v = map(int, input().split())
    link[u].append(v)
    link[v].append(u)
for arr in link:
    arr.sort()

cnt = 1
visited = [0] * (n + 1)
visited[r] = 1
q = deque([r])  # r을. 꺼낸다.??
while (q):
    a = q.popleft()  # 원래 pop 방향의 반대에서 pop (q에서 pop)
    for i in link[a]:
        if visited[i]:
            continue
        cnt += 1
        visited[i] = cnt
        q.append(i)

for j in range(1, n + 1):
    print(visited[j])
