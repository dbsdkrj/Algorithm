import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**4)
'''
while (1) 이었을 땐 런타임에러
q의 길이가 1이기 전까지 반복하라고 수정하니 정답
'''

n = int(input())
q = deque([i for i in range(1,n+1)])

while (len(q)>1):
    q.popleft()
    q.append(q.popleft())
    if len(q) == 1:
        break

print(q[0])