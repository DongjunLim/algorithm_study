import sys
sys.stdin = open("input.txt","r")

T = int(input())


for tc in range(1,T+1):
    answer = 0
    N, M = map(int, input().split())

    A = [input() for _ in range(N)]
    B = [input() for _ in range(M)]

    for b in B:
        length = len(b)

        for a in A:
            if len(a) < length:
                continue
            if b in a[:length]:
                answer += 1
                break

    print(f'#{tc} {answer}')
