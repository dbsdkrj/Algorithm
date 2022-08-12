#다시 풀기 0801

import sys
from collections import deque

# input = sys.stdin.readline()

t = int(sys.stdin.readline())

for _ in range(t):
    p = deque(list(sys.stdin.readline().rstrip()))  # [R, D, D]
    n = int(sys.stdin.readline())  # 4
    x = deque(list(sys.stdin.readline().rstrip()))  # [1, 2, 3, 4]
    x.pop()
    x.popleft()
    for i in range(1, n):
        x.remove(",")
    print(x)
    while len(p) != 0:
        if p[0] == "R":
            x.reverse()
            p.popleft()
        if p[0] == "D":
            if len(x) == 0:
                print("error")
                break
            else:
                x.popleft()
                p.popleft()
    print(x)

# for _ in range(t):
#     # p = deque(list(map(str,input().split())))
#     # n = int(input())
#     tmp = list(input())
#     x = deque()
#     for i in tmp:
#         if i not in "[],":
#             x.append(tmp[i])
#     # tmp = ''.join( x for x in tmp if x not in ("[],"))
#     print(x)

#     # while(len(p)!=0):
#     #     if p[0] == ""