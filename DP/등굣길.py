'''
    동적계획법을 사용해 풀었습니다.
    n x m 배열(board)을 만들고, 배열의 값을 집(1,1)에서 각 위치까지의 최단경로의 경우의 수를 저장하고,
    목적지인덱스에 담긴 값(board[n][m])을 반홥했습니다.
'''


def is_possible(row, col, board):
    """ board[row][col]이 웅덩이인지 확인. """

    return True if board[row][col] > -1 else False


def calc_number_of_case(row, col, board):
    """ board[row][col]에서의 최단경로 경우의 수 계산. """

    if is_possible(row, col-1, board):
        board[row][col] += board[row][col-1]
    if is_possible(row-1, col, board):
        board[row][col] += board[row-1][col]
    return


def set_board(m, n, board, puddles):
    """ 지도 세팅. """

    for i in range(1, n+1):
        for j in range(1, m+1):
            if [j, i] in puddles:
                board[i][j] = -1
            else:
                board[i][j] = 0


def solution(m, n, puddles):
    """ 배열을 순회하며 각 집(1,1)에서 각 지점까지의 최단경로 경우의 수를 갱신. """
    board = [[-1] * (m+2) for _ in range(n+2)]

    set_board(m, n, board, puddles)

    board[1][1] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if not is_possible(i, j, board):
                continue
            calc_number_of_case(i, j, board)

    # 목적지의 최단경로값 반환
    return board[n][m] % 1000000007


def main():

    m, n = 4, 3
    puddles = [[1, 3], [3, 1]]

    print(solution(m, n, puddles))


if __name__ == '__main__':
    main()