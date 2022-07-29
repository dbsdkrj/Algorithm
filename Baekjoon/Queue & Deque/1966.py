#선입선출
import sys
input = sys.stdin.readline
from collections import deque

num = int(input())

for _ in range(num):
    n, m = map(int, input().split())
    arr = deque(map(int, input().split()))
    idx = deque(range(0,n))

    cnt = 0

    while arr:
        if arr[0] == max(arr):
            cnt += 1
            arr.popleft()
            if idx.popleft() == m:
                print(cnt)
                break
        else:
            arr.rotate(-1)
            idx.rotate(-1)