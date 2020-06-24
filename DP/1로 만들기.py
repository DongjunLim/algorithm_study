import sys
sys.stdin = open("input.txt","r")

N = int(input())
INF = N+1
answer = INF
dp = [INF] * (N+3)
dp[1] = 0
dp[2] = 1
dp[3] = 1

now = 4
for i in range(now,N+1):

    if i % 3 == 0:
        dp[i] = min(dp[i//3],dp[i-1])
    if i % 2 == 0:
        dp[i] = min(dp[i//2],dp[i])

    dp[i] = min(dp[i],dp[i-1])

    dp[i] += 1

print(dp)
print(dp[N])
