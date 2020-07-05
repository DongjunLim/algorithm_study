def is_possible(row, col, board):
    return True if board[row][col] > -1 else False


def solution(m, n, puddles):
    board = [[-1] * (m+2) for _ in range(n+2)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if [j, i] in puddles:
                board[i][j] = -1
            else:
                board[i][j] = 0

    # 기저사례
    if board[1][2] is not -1:
        board[1][2] = 1
    if board[2][1] is not -1:
        board[2][1] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if board[i][j] == -1:
                continue
            if is_possible(i, j-1, board):
                board[i][j] += board[i][j-1]
            if is_possible(i-1, j, board):
                board[i][j] += board[i-1][j]

    return board[n][m] % 1000000007 if board[n][m] > 0 else 0


def main():

    m, n = 4, 3
    puddles = [[1, 3], [3, 1]]

    print(solution(m, n, puddles))


if __name__ == '__main__':
    main()