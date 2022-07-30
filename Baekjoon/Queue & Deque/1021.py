import sys
input = sys.stdin.readline
from collections import deque
'''
arr.index(out[0]) <= (len(arr)-arr.index(out[0])-1)
에서 <= 대신 < 써서 오답이었음
'''

n, m = map(int, input().split())
out = deque(map(int,input().split()))
arr = deque([i for i in range(1,n+1)])
cnt = 0

while len(out) !=0:
    if arr[0] == out[0]:
        arr.popleft()
        out.popleft()
    else:
        if arr.index(out[0]) <= (len(arr)-arr.index(out[0])-1):
            arr.rotate(-1)
            cnt +=1
        else:
            arr.rotate(1)
            cnt +=1
print(cnt)
