T=int(input())
for _ in range(T):
    n = int(input())
    dp=[0,1,2,4]
    for i in range(4,n+1):
        dp.append(dp[i-1]+dp[i-2]+dp[i-3])
    print(dp[n])
'''
1:1
2:2
3:4
4:7
5:13
6:24
111111->1
11112->5
1113->4
1122->6
123->6
222->1
33->1
'''
