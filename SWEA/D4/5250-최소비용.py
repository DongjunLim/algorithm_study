import sys
sys.stdin = open("input.txt","r")
INF = 9999999999
T = int(input())

def around(i,j):
    global board, boardCost, N

    if i == 0:
        up = 0
    else:
        up = boardCost[i-1][j] + (0 if board[i][j]-board[i-1][j] <= 0 else board[i][j]-board[i-1][j]) + 1

    if i == N-1:
        down = 0
    else:
        down = boardCost[i+1][j] + (0 if board[i][j]-board[i+1][j] <= 0 else board[i][j]-board[i+1][j]) + 1

    if j == 0:
        left = 0
    else:
        left = boardCost[i][j-1] + (0 if board[i][j]-board[i][j-1] <= 0 else board[i][j]-board[i][j-1]) + 1

    if j == N-1:
        right = 0
    else:
        right = boardCost[i][j+1] + (0 if board[i][j]-board[i][j+1] <= 0 else board[i][j]-board[i][j+1]) + 1

    now = boardCost[i][j]

    if i == 0:
        if j == 0:
            boardCost[i][j] = min([now,down,right])
        elif j == N-1:
            boardCost[i][j] = min([now,down,left])
        else:
            boardCost[i][j] = min([now,down,left,right])
        return

    if i == N-1:
        if j == 0:
            boardCost[i][j] = min([now,up,right])
        elif j == N-1:
            boardCost[i][j] = min([now,up,left])
        else:
            boardCost[i][j] = min([now,up,left,right])
        return

    if j == 0:
        boardCost[i][j] = min([now,up,down,right])
        return

    if j == N-1:
        boardCost[i][j] = min([now,up,down,left])
        return

    boardCost[i][j] = min([now,up,down,left,right])
    return


for tc in range(1,T+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    boardCost = [[INF]*N for _ in range(N)]
    boardCost[0][0] = 0
    for i ,x in enumerate(board):
        for j, y in enumerate(x):
            around(i,j)
            if i != 0:
                around(i-1,j)
            if j != 0:
                around(i,j-1)
            if i != N-1:
                around(i+1,j)
            if j != N-1:
                around(i,j+1)

    print(f'#{tc} {boardCost[N-1][N-1]}')
