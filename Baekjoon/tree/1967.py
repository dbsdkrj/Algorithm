from math import dist
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
V = int(input())
tree = [[] for _ in range(V+1)]

def dfs(node, weight):
    for i in tree[node]:
        x, y = i #함수 인자 node에 연결된 x, 가중치 y
        if distance[x] == -1:  #방문하지 않았으면
            distance[x] = weight+y  #가중치 업데이트
            dfs(x, weight+y)

for _ in range(V-1):
    a, b, c = map(int, input().split())
    tree[a].append([b,c]) #a노드에 연결된 b, 가중치 c
    tree[b].append([a,c]) #b노드에 연결된 a, 가중치 c

distance = [-1] * (V+1)
distance[1] = 0
dfs(1, 0)

start = distance.index(max(distance))
distance = [-1] * (V+1)
distance[start]=0
dfs(start, 0)

print(max(distance))