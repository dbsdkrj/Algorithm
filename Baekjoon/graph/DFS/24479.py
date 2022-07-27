import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m, r = map(int,input().split()) #정점의 수, 간선의 수, 시작 정점
link = [[] for _ in range(n+1)] #[ [ None ], [노드1用], [ 노드2用], ... ]

for i in range(m): #간선 수만큼
    u, v = map(int, input().split())  # 1, 2
    '''
       1   2 
    1 [ ] [ ]
    2 [ ] [ ]
    '''
    #양방향 간선
    link[u].append(v)  #(u,v)
    link[v].append(u)  #(v,u)

for arr in link:
    arr.sort()  #오름차순

cnt = 1  #방문 순서
visited = [0]*(n+1)  #방문 여부
def dfs(x): #노드x 방문
    global cnt
    visited[x] = cnt  #노드x에 방문함을 표시
    for k in link[x]:  #노드x와 연결된 노드들 방문
        if visited[k]:  #노드x와 연결된 노드들이 이미 방문됐었으면 pass
            continue
        cnt += 1 #다음 방문 순서 표기를 위해 +1
        dfs(k) #재귀
dfs(r)  #처음 방문하는 노드는 r

for j in range(1, n+1):
    print(visited[j])
