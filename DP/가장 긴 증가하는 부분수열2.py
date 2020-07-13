import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
INF = 1001

def bSearch(c, target):
    left, right = 0, len(c) -1

    while left <= right:
        mid = (left + right) // 2

        if target == c[mid]:
            return mid

        elif target < c[mid]:
            if target > c[mid-1]:
                return mid
            right = mid

        elif target > c[mid]:
            if target < c[mid+1]:
                return mid+1
            left = mid + 1

    return mid


def solution(n, a):
    global INF
    c = [INF] * (n+1)
    c[0] = -1
    maxIdx = -1
    for i in range(n):
        idx = bSearch(c, a[i])
        c[idx] = a[i]
        if idx >= maxIdx:
            maxIdx = idx
            answer = ''
            for k in range(1, maxIdx):
                answer += str(c[k])
                answer += ' '
            answer += str(c[maxIdx])

    print(maxIdx)
    print(answer)

    return

def main():
    N = int(input())
    A = list(map(int, input().split()))

    solution(N,A)

if __name__ == '__main__':
    main()