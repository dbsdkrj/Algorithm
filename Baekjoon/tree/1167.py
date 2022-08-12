import sys
from collections import deque
input = sys.stdin.readline

V = int(input())
tree = [[] for _ in range(V+1)]

for i in range(V):
    tmp = list(map(int, input().split()))
    for j in range(1, len(tmp)-2, 2):
        tree[tmp[0]].append((tmp[j], tmp[j+1]))
        #첫번째 노드와 연결된 (노드번호, 거리)

def bfs(start):
    visited = [-1] * (V+1)
    q = deque([start])
    visited[start]=0
    result = [0,0]
        #[ 최대 거리, 정점 ]
    while q:
        x = q.popleft()
        for i, j in tree[x]: #x와 연결된 노드번호, 거리
            if visited[i] == -1: #방문하지 않았다면
                visited[i] = visited[x] + j #거리 갱신
                    #(시작점(1)과 x노드의 거리 + x노드와 해당 노드의 거리)
                q.append(i)  #큐에 x와 연결된 노드 저장
                if result[0] < visited[i]:  #최대 거리 < x와 연결된 노드와 시작점 거리
                    result = visited[i],i #최대거리 갱신 = [최대거리, 정점]
    return result

distance, node = bfs(1)  # 1에서 가장 먼 노드 찾기
distance, node = bfs(node) #위 노드에서 가장 먼 노드 찾기

print(distance)