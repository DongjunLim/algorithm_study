def solution(n):
    INF = 999999999
    cnt = (n // 15) * 3
    mod = n % 15

    dp = [INF] * n+1

    dp[3], dp[5] = 1, 1

    for i in range(6, n+1):
        dp[i] = min(dp[i-3] + 1, dp[i-5] + 1)

    if dp[n] >= INF:
        return -1

    return dp[n]


def main():
    N = int(input())

    print(solution(N))


if __name__ == '__main__':
    main()