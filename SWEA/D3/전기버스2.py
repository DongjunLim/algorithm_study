import sys
import time
sys.stdin = open("input.txt","r")
T = int(input())
INF = 999999999

def dfs(idx, cnt, battery):
    global answer, busStops
    if idx+1 == N:
        answer = min(answer,cnt)
        return

    if answer <= cnt:
        return

    changedBattery = busStops[idx]

    if battery < changedBattery:
        dfs(idx+1,cnt+1, changedBattery-1)
    if battery > 0:
        dfs(idx+1,cnt, battery-1)

    return


start = time.time()
for tc in range(1,T+1):
    answer = INF
    cnt = 0
    busStops = list(map(int,input().split()))
    N = busStops.pop(0)
    dp = [0] * N

    dfs(1,0,busStops[0]-1)


    print(f'#{tc} {answer}')

ms = (time.time() - start) * 1000
print(f'백트래킹: {round(ms,4)}ms')