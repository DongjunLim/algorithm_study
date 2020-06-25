import sys
sys.stdin = open("input.txt","r")


N = int(input())

cardPacks = list(map(int, input().split()))

dp = [0] * (N+1)

for i in range(1,N+1):
    for j in range(1,i+1):
        dp[i] = max(dp[i], dp[i-j]+cardPacks[j-1])
print(dp[N])