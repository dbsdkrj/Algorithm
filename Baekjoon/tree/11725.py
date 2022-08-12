#parent 갱신하고 큐 삽입
#큐에서 popleft하고 다시 반복.
#큐가 비면 종료
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    i, j = map(int, input().split())
    tree[i].append(j)
    tree[j].append(i)

def bfs():
    parent=[0 for _ in range(N+1)] #부모 노드 저장
    q = deque([1])  #검사할 노드 차례대로 입력할 큐
    while q:
        x = q.popleft()
        for i in tree[x]:
            if parent[i] == 0 and i!=1:
                parent[i]=x
                q.append(i)
    for i in parent[2:]:
        print(i)

bfs()