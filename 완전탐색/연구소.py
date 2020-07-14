import sys
from collections import deque
sys.stdin = open("input.txt", "r")

answer = 0
n, m = 0, 0
visited = []
board = []
checked = []
virus = []
numberOfZero = 0
zero_list = []
dt = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def check_out_of_range(row, col):
    global n, m, board
    if row < 0 or n <= row or col < 0 or m <= col:
        return False

    if board[row][col] == 0:
        return True

    return False


def count_zero_area():
    global n, m, board, zero_list
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                cnt += 1
                zero_list.append((i, j))

    return cnt


def check_safe_area():
    global virus, checked, numberOfZero
    checked = [[False] * m for _ in range(n)]

    infection_count = 0

    for x, y in virus:
        infection_count += bfs(x, y)

    return numberOfZero - infection_count - 3


def bfs(row, col):
    global virus, board, checked, dt
    queue = deque()

    queue.append((row, col))
    checked[row][col] = True
    cnt = 0

    while queue:
        r, c = queue.pop()

        for x, y in dt:
            next_r = r+x
            next_c = c+y
            if check_out_of_range(next_r, next_c) and not checked[next_r][next_c]:
                checked[next_r][next_c] = True
                queue.append((next_r, next_c))
                cnt += 1

    return cnt


def get_combination(wall_cnt, rg):
    global visited, board, n, m, zero_list, numberOfZero, answer

    if wall_cnt == 3:
        now = check_safe_area()
        answer = max(now, answer)
        return

    for i in range(rg, numberOfZero):
        r, c = zero_list[i]

        if board[r][c] == 0 and not visited[i]:
            visited[i] = True
            board[r][c] = 1
            get_combination(wall_cnt + 1, rg + 1)
            board[r][c] = 0
            visited[i] = False


def solution(n, m):
    global visited, board, zero_list, answer

    visited = [False] * numberOfZero

    get_combination(0, 0)

    return answer


def main():
    global board, n, m, numberOfZero
    n, m = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                virus.append((i, j))
    numberOfZero = count_zero_area()

    print(solution(n, m))


if __name__ == '__main__':
    main()