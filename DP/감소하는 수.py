import sys
sys.stdin = open("input.txt", "r")

def is_desc(number):
    itoa = str(number)
    length = len(itoa)

    for i in range(1, length):
        if itoa[i-1] <= itoa[i]:
            return False

    return True




def solution(n):
    if n > 1023:
        return -1

    dp = [0] * (n + 1)

    for i in range(11):
        dp[i] = i

    idx = 11
    number = 11

    while idx <= n:
        if is_desc(number):
            dp[idx] = number
            idx += 1

        number += 1

    return dp[n]


def main():
    n = int(input())

    print(solution(n))


if __name__ == '__main__':
    main()