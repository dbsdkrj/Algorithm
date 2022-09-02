from collections import deque
import sys

sys.setrecursionlimit(1000)
input = sys.stdin.readline

def dfs(s, arr, visited):
    visited[s] = True
    for i in arr[s]:
        if not visited[i]:
            dfs(i, arr, visited)


def solution(n, computers):
    cnt = 0
    visited = [0] * (n + 1)  # 0~n-1

    # 사용할 배열 다시 만들기 !!
    arr = [[] for _ in range(n + 1)]
    for i in range(n):  # 012
        for j in range(n):  # 012
            if i == j:
                continue
            else:
                if computers[i][j] == 1:
                    arr[i + 1].append(j + 1)

    for i in range(1, n):
        if not visited[i]:
            dfs(i, arr, visited)
            cnt += 1

    for i in range(1, n + 1):
        if visited[i] == 0:
            cnt += 1
    return cnt


# bfs(0)로 1과 연결된 애들 찾고 visited에 저장
# bfs(1)부터 bfs(n-1)까지 검사

'''
arr
[
[]
[2]
[1]
[]
]

visited
[ 0, 1, 1, 0]
'''

#다시 풀어봄


def dfs(a, arr, visited):
    visited[a] = 1
    for i in arr[a]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i, arr, visited)


def solution(n, computers):
    visited = [0 for _ in range(n + 1)]
    # 코딩에서 쓸 배열 새로 만들기
    # 전에 풀어봤던 연결요소 개수 세기 문제처럼
    arr = [[] for _ in range(n + 1)]

    for i in range(n):
        for j in range(n):
            if j == i:
                continue
            else:
                if computers[i][j] == 1:  # computers[0][1]
                    arr[i + 1].append(j + 1)

    cnt = 0
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i, arr, visited)
            cnt += 1

    answer = cnt
    return answer