import sys
sys.stdin = open("input.txt","r")
T = int(input())


for _ in range(T):
    N = int(input())
    dp = [1,1,3,3]
    start = len(dp)
    if start > N:
        print(dp[N])
    else:
        for num in range(start,N+1):
            dp.append((dp[-1]+dp[-2]+dp[-3])%1_000_000_000_9)

    print(dp[-1])