import sys
print = sys.stdout.write
sys.stdin = open("input.txt", "r")
answer = 0
visited = []
dp = []


def backtracking(date, half, full):
    global answer, dp

    if not half and not full:
        return 1

    if dp[half][full] > 0:
        return dp[half][full]

    if half:
        dp[half][full] = backtracking(date+1, half-1, full)

    if full:
        dp[half][full] += backtracking(date+1, half+1, full-1)

    return dp[half][full]


def solve(n):
    global answer, visited, dp

    dp = [[0] * (n+1) for _ in range(n+1)]
    answer = 0

    return backtracking(1, 0, n)


def main():
    global print

    while True:
        N = int(input())
        if N == 0:
            return
        print(f'{solve(N)}\n')


if __name__ == "__main__":
    main()