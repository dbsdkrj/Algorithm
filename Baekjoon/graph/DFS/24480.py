import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m, r = map(int,input().split())
link = [[] for _ in range(n+1)] #간선[ [ ], [ ], [ ], [ ], [ ] ]

for i in range(m):
    u, v = map(int, input().split())  # 1, 2
    '''
       1   2
    1 [ ] [ ]
    2 [ ] [ ]
    '''
    link[u].append(v)
    link[v].append(u)

for arr in link:
    arr.sort(reverse=True)

cnt = 1
visited = [0]*(n+1)
def dfs(v):
    global cnt
    visited[v] = cnt
    for k in link[v]:
        if visited[k]:  #not 0
            continue
        cnt += 1
        dfs(k)
dfs(r)

for j in range(1, n+1):
    print(visited[j])
