import sys
sys.stdin = open("input.txt","r")


N = int(input())

cardPacks = list(map(int, input().split()))

dp = [10000000] * (N+1)
dp[1] = cardPacks[0]
dp[0] = 0

for i in range(1,N+1):
    for j in range(1,i+1):
        dp[i] = min(dp[i], dp[i-j]+cardPacks[j-1])
print(dp[N])