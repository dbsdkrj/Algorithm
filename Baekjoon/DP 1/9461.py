'''
1
1
1
2
2
3
4
5
7
9
12
16  --> N=4 부터 규칙 시작 (전전전 숫자와 전전 숫자의 합)
'''

dp = [0] * (101)
dp[1]=1
dp[2]=1
dp[3]=1
for i in range(0,98):
    dp[i+3] = dp[i]+dp[i+1]
# for i in range(4, N+1):  --> 이렇게 했더니 틀림(런타임에러)
#     dp[i] = dp[i-3]+dp[i-2]
T = int(input())
for _ in range(T):
    N = int(input())
    print(dp[N])