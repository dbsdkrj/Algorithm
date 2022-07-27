import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque
'''
visited한 컴퓨터(노드) 개수 세기
if visited[i] != 0:
    cnt+=1
bfs로 풀이
'''
n = int(input())
m = int(input())
link = [[] for _ in range(n+1)]

for i in range(m):
    u, v = map(int, input().split())
    link[u].append(v)
    link[v].append(u)

visited = [0] * (n+1)

#BFS
def bsf():
    q = deque([1])
    global visited
    visited[1] = True
    while(q):
        a = q.popleft()
        for i in link[a]:
            if visited[i]: #0이 아니면 pass
                continue
            visited[i] = True
            q.append(i)
bsf()

print(visited.count(True)-1)