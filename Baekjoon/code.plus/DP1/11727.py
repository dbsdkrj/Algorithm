import sys
input = sys.stdin.readline
n = int(input())
'''
1-1
2-3
3-5
4-11
5-21
'''
dp=[0, 1, 3]
for i in range(3,n+1):
    dp.append(dp[i-1]+dp[i-2]*2)
print(dp[n]%10007)
