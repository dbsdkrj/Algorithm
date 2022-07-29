import sys

input = sys.stdin.readline
from collections import deque

'''
pop에서 q.pop(0)이 아니라 q.popleft() 쓰니까 정답
'''

n = int(input())
q = deque()
for _ in range(n):
    order = []
    order = input().split()

    if order[0] == "push":
        q.append(order[1])

    if order[0] == "pop":
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())

    if order[0] == "size":
        print(len(q))

    if order[0] == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)

    if order[0] == "front":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])

    if order[0] == "back":
        if len(q) == 0:
            print(-1)
        else:
            print(q[len(q) - 1])
