n = int(input())
arr = []
rank = []

for _ in range(n):
    kg, cm = map(int, input().split())
    arr.append((kg, cm))

for i in range(n):
    cnt = 0
    for j in range(n):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            cnt += 1
    rank.append(cnt + 1)  # 자신보다 "큰" 덩치인 사람 수 +1

for k in range(n):
    print(rank[k], end=" ")