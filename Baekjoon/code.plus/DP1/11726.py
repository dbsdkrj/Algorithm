'''
1-1
2-2
3-3
4-5
5-8
6-1+6+5+1=13
'''
#런타임에러(IndexError)
n = int(input())
dp=[0 for _ in range(n+1)]
dp[1]=1
dp[2]=2
for i in range(3,n+1):
    dp[i] = dp[i-1]+dp[i-2]
print(dp[n]%10007)

#정답
n = int(input())
dp=[0, 1, 2]
for i in range(3,n+1):
    dp.append(dp[i-1]+dp[i-2])
print(dp[n]%10007)
