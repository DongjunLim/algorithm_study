import sys
sys.stdin = open("input.txt", "r")


def solution(n, a):
    lis = []

    for x in a:
        lis.append(x)


    for i in range(n):
        for j in range(i):
            if a[i] > a[j] and lis[i] < lis[j] + a[i]:
                lis[i] = lis[j] + a[i]

    print(max(lis))


def main():
    N = int(input())
    A = list(map(int, input().split()))

    solution(N, A)


if __name__ == '__main__':
    main()