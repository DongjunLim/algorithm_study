import sys
sys.stdin = open("input.txt","r")
sys.stdin.readline

T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())

    W = list(map(int,input().split()))
    T = list(map(int,input().split()))

    answer = 0

    W.sort(reverse=True)
    T.sort(reverse=True)

    DP = [False] * len(W)

    for t in T:
        for i, w in enumerate(W):
            if t >= w and DP[i] == False:
                answer += w
                DP[i] = True
                break

    print(f'#{tc} {answer}')


