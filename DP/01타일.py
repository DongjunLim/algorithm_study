
def solution(n):
    dp = [0] * (n+1)

    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3

    dp[1] = 1
    dp[2] = 2
    dp[3] = 3

    for i in range(4, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 15746

    return dp[n] % 15746


def main():
    N = int(input())

    print(solution(N))

if __name__ == '__main__':
    main()