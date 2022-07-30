import sys

input = sys.stdin.readline
from collections import deque

n = int(input())
q = deque()
for _ in range(n):
    order = []
    order = input().split()

    if order[0] == "push_front":
        q.appendleft(order[1])

    if order[0] == "push_back":
        q.append(order[1])

    if order[0] == "pop_front":
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())

    if order[0] == "pop_back":
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop())

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
