# 리모컨
import sys

input = sys.stdin.readline
goal = int(input())
n = int(input())
if n != 0:
    trouble_number = list(map(int, input().split()))
else:
    trouble_number = []

cnt = abs(100 - goal)

for i in range(1000001):
    num = str(i)

    for k in range(len(num)):
        if int(num[k]) in trouble_number:  # 고장난 숫자가 있으면 break
            break

        elif k == len(num) - 1:
            cnt = min(cnt, abs(int(num) - goal) + len(num))
            # 100부터 ±버튼 눌러서 목표 도달
            # vs.
            # num까지 누르고(len(num)) ±버튼 누르기(int(num)-goal)

print(cnt)
