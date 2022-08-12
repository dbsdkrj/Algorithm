n = int(input())
seq = list(map(int, input().split()))
 # seq = [ 10 -4 3 1 5 6 -35 12 21 -1 ]
dp = [0] * (n)
dp[0] = seq[0]
 # dp = [ 10 0 0 0 0 0 0 0 ... ]

for i in range(1,n):
    dp[i] = max(seq[i], seq[i]+dp[i-1])
'''
dp[0] = 10
dp[1] = max(seq[1], seq[1]+dp[0])  #-4 vs. 10-4     -> 6
dp[2] = max(seq[2], seq[2]+dp[1])  # 3 vs. 3+6      -> 9
dp[3] = max(seq[3], seq[3]+dp[2])  # 1 vs. 1+9      -> 10
dp[4] = max(seq[4], seq[4]+dp[1])  # 5 vs. 5+10     -> 15
dp[5] = max(seq[5], seq[5]+dp[1])  # 6 vs. 6+15     -> 21
dp[6] = max(seq[6], seq[6]+dp[1])  # -35 vs. -14    -> -14
dp[7] = max(seq[7], seq[7]+dp[1])  # 12 vs. -2      -> 12
dp[8] = max(seq[8], seq[8]+dp[1])  # 21 vs. 33      -> 33
dp[9] = max(seq[9], seq[9]+dp[1])  # -1 vs. 32      -> 32
'''
print(max(dp))  #33