n = int(input())
dp = [0]*(n+1)
for i in range(2,n+1):
    dp[i] = dp[i-1]+1
    if i%2==0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i%3==0:
        dp[i] = min(dp[i], dp[i//3]+1)
print(dp[n])
'''
dp[2] => 1번
dp[3] => 1번
dp[4] => 2번
dp[5] => 3번
dp[6] => 2번 : 2로 만드는 연산 1번 + dp[2] = 2  vs. 3으로 만드는 연산 + dp[3]
dp[7] => 3번 : 6으로 만드는 연산 1번 + dp[6] = 3 
dp[8] => 4번 : 4로 만드는 연산 1번 + dp[6] = 3
dp[9] => 2번 : 3으로 만드는 연산 1번 + dp[3] = 2
dp[10]=> 3번 : dp[9]+1(=3)  vs  5로 만드는 연산 + dp[5](=4)  => 3

"이전 n"으로 가는 연산 1번 + dp["이전 n"] = dp[i-1]+1
☝🏻이거랑 2로 나눌 경우랑 3으로 나눌 경우를 비교..!

'''