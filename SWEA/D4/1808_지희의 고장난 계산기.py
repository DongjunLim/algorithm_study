import sys
from collections import deque
sys.stdin = open("input.txt", "r")

INF = 999999999


def solution(target, numbers):
    global INF
    usable = []
    dp = [INF] * (target + 10)

    for i, x in enumerate(numbers):
        if x:
            usable.append(i)
            dp[i] = 2

    for i in range(target+1):
        for num in usable:
            if num and i % num == 0:
                dp[i] = min(dp[i], dp[i//num] + 2)

            if i > 9 and i % 10 == num:
                dp[i] = min(dp[i], dp[i//10] + 1)

    return dp[target] if dp[target] != INF else -1


def main():
    T = int(input())

    for tc in range(1, T+1):
        numbers = list(map(int, input().split()))
        target = int(input())

        print(f'#{tc} {solution(target, numbers)}')


if __name__ == '__main__':
    main()