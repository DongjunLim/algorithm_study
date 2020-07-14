import sys
sys.stdin = open("input.txt", "r")


def solution(n, a):
    lis = [[0] * 2 for _ in range(n)]
    lis[0][0] = a[0]
    lis[0][1] = a[0]
    answer = a[0]
    for i in range(1, n):
        lis[i][0] = max(a[i], lis[i-1][0] + a[i])
        lis[i][1] = max(lis[i-1][0], lis[i-1][1] + a[i])
        answer = max(answer, max(lis[i]))

    return answer


def main():
    n = int(input())
    a = list(map(int, input().split()))

    print(solution(n, a))


if __name__ == '__main__':
    main()