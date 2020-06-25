N = int(input())

def solution(n):
    global dp

    if n == 1:
        dp[1] = 1
        return 1
    elif n == 2:
        dp[2] = 2
        return 2

    if dp[n] != -1:
        return dp[n]

    dp[n] = solution(n-2) + solution(n-1)

    return dp[n]

dp = [-1] * (N+1)

print(solution(N)%10007)

