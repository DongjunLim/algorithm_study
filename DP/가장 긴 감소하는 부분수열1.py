import sys
sys.stdin = open("input.txt", "r")


def solution(n, a):
    lis = [1] * n

    for i in range(n):
        for j in range(i):
            if a[j] > a[i] and lis[j] + 1 > lis[i]:
                lis[i] = lis[j]+1

    return max(lis)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(solution(N, A))


if __name__ == '__main__':
    main()