import sys
sys.stdin = open("input.txt","r")

T = int(input())



for tc in range(1, T+1):

    N, M, X, Y = map(int,input().split())

    board = [list(map(int,input().split())) for _ in range(M)]

    K = int(input())
    kValue = list(map(int, input().split()))

    L = int(input())
    orders = [list(map(str, input().split())) for _ in range(L)]
    visited = [[False]*(N) for _ in range(M)]

    k = 0
    row = Y-1
    col = X-1
    answer = board[row][col]
    # print(answer)
    visited[row][col] = True
    for nowOrder in orders:
        direction = nowOrder[0]     # 움직일 방향
        rotation = nowOrder[1]      # 회전판 방향
        rotateCnt = nowOrder[2]     # 회전판 얼만큼 돌릴지

        # 우측으로 회전판을 돌린다.
        if rotation == '2':
            k = (k+int(rotateCnt))%K
            movement = kValue[k]

        # 좌측으로 회전판을 돌린다.
        elif rotation == '1':
            k = (k-int(rotateCnt))%K
            movement = kValue[k]



        if direction == 'E':
            for i in range(movement):
                if col == N-1:
                    break
                if board[row][col+1] == -1:
                    break
                col += 1

                if not visited[row][col]:
                    visited[row][col] = True
                    answer += board[row][col]

        elif direction == 'W':
            for i in range(movement):
                if col == 0:
                    break
                if board[row][col-1] == -1:
                    break
                col -= 1

                if not visited[row][col]:
                    visited[row][col] = True
                    answer += board[row][col]

        elif direction == 'S':
            for i in range(movement):
                if row == M-1:
                    break
                if board[row+1][col] == -1:
                    break
                row += 1
                if not visited[row][col]:
                    visited[row][col] = True
                    answer += board[row][col]

        elif direction == 'N':
            for i in range(movement):
                if row == 0:
                    break
                if board[row-1][col] == -1:
                    break
                row -= 1
                if not visited[row][col]:
                    visited[row][col] = True
                    answer += board[row][col]

    print(f'#{tc} {answer} {col+1} {row+1}')