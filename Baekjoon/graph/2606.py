import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque
'''
visited한 컴퓨터(노드) 개수 세기
if visited[i] != 0:
    cnt+=1
dfs로 풀이
'''
n = int(input())
m = int(input())
link = [[] for _ in range(n+1)]

for i in range(m):
    u, v = map(int, input().split())
    link[u].append(v)
    link[v].append(u)

visited = [0] * (n+1)

#변형
def dsf(a):
    visited[a]=1
    for j in link[a]:
        if visited[j]: #j가 0이 아니면 pass
            continue
        dsf(j)

dsf(1)

print(visited.count(1)-1)