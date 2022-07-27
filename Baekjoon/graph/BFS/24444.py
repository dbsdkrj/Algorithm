import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
from collections import deque

n, m, r = map(int, input().split())  #정점의 수, 간선의 수, 시작 정점
link = [[] for _ in range(n + 1)]  #[ [ None ], [노드1用], [ 노드2用], ... ]

# 양방향 간선
for _ in range(m):  #간선 수만큼
    u, v = map(int, input().split())
    link[u].append(v)  #노드 u 링크리스트에 v추가
    link[v].append(u)  #노드 v 링크리스트에 u추가
for arr in link:
    arr.sort()

cnt = 1
visited = [0] * (n + 1)  #방문 여부 리스트
visited[r] = 1 #첫번째 노드의 방문 순서는 1
q = deque([r])  # 첫번째 노드가 들어있는 큐를 하나 만든다.  q = [r]
'''
deque = 양방향 연결리스트. 양끝에 접근 가능
    #append, appendleft, pop, popleft
'''
while (q): #q가 비어있을 때까지 반복
    a = q.popleft()  # q의 왼쪽에서 pop하고 a에 저장 a=r, q=[]
    for i in link[a]:  #노드 a에 연결된 노드들 = i
        if visited[i]:  #노드 i를 방문했었다면 pass
            continue
        cnt += 1  #방문 순서 +1
        visited[i] = cnt  #i번째 노드를 방문했다고 표시
        q.append(i) #q에 i 추가

for j in range(1, n + 1):
    print(visited[j])
