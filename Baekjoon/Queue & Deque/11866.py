import sys
input= sys.stdin.readline
from collections import deque
'''
k=3 고정인줄 알고 q.rotate(-2) 해서 계속 오답 ㅜㅜ
'''

n, k = map(int,input().split())
q=deque([i for i in range(1,n+1)])
perm = []

while (len(q)!=0) :
    q.rotate(-(k-1))
    perm.append(q.popleft())
    #rotate(n) : n만큼 오른쪽으로 이동
    #rotate(-n) : n만큼 왼쪽으로 이동

print(f'<{", ".join(map(str,perm))}>')