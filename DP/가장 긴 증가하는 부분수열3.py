import sys
sys.stdin = open("input.txt", "r")


def solution(n, a):
    lis = [1] * n
    lisSet = [set() for _ in range(n)]
    lisSet[0].add(a[0])
    maxIdx = -1
    for i in range(n):
        lisSet[i] = set()
        lisSet[i].add(a[i])
        for j in range(i):
            if a[j] < a[i] and lis[j] + 1 > lis[i]:
                lis[i] = lis[j]+1
                lisSet[i] = set()
                for x in lisSet[j]:
                    lisSet[i].add(x)
                lisSet[i].add(a[i])

        if lis[maxIdx] < lis[i]:
            maxIdx = i


    result = list(lisSet[maxIdx])
    result.sort()
    answer = ''
    for x in result[:-1]:
        answer += str(x)
        answer += ' '

    answer += str(result[-1])
    print(lis[maxIdx])
    print(answer)

    return max(lis)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    solution(N, A)

if __name__ == '__main__':
    main()