n, m = map(int, input().split())
card = list(map(int, input().split()))
judge = 0

for k in range(n): #0 1 2 3 4
    for j in range(k+1,n): #1 2 3 4
        for i in range(j+1,n): # 2 3 4
            sum = card[k]+card[j]+card[i]
            if sum <= m:
                judge = max(judge, sum)
                # if m - sum < judge:  #오답
                #     judge = sum
print(judge)

