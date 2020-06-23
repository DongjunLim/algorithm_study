import sys
import time
sys.stdin = open("input.txt","r")
T = int(input())
INF = 999999999

start = time.time()
for tc in range(1,T+1):
    answer = INF
    cnt = 0
    busStops = list(map(int,input().split()))
    N = busStops.pop(0)
    dp = [INF] * N
    dp[-1] = 0

    length = len(dp)-1

    for i in range(length-1,-1,-1):
        now = busStops[i]

        for j in range(i+1,i+now+1):
            if len(dp) <= j:
                break
            dp[i] = min(dp[i],dp[j])

        dp[i] += 1


    print(f'#{tc} {dp[0]-1}')

ms = (time.time() - start) * 1000
print(f'DP: {round(ms,4)}ms')