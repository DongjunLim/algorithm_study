import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    answer = 0

    tile = [0] * (N+1)
    tile[1] = 1
    tile[2] = 3
    tile[3] = 6

    for i in range(4, N+1):
        tile[i] = tile[i-1] + tile[i-2]*2 + tile[i-3]

    answer = tile[N]
    print(f'#{tc} {answer}')