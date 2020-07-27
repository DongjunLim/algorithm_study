import sys
from collections import deque
sys.stdin = open("input.txt")
N, M = 0, 0
dt = [[0, -1], [0, 1], [-1, 0], [1, 0]]


def check_out_of_range(r, c):
    global N, M
    if r < 0 or N <= r or c < 0 or M <= c:
        return False
    return True


def bfs(sr, sc, board):
    global N, M, dt

    queue = deque()
    visited = [[False] * M for _ in range(N)]

    visited[sr][sc] = True
    queue.append((sr, sc, 1))

    while queue:
        r, c, cnt = queue.popleft()
        if r == N-1 and c == M-1:
            return cnt

        for x, y in dt:
            nr, nc = r+x, c+y

            if check_out_of_range(nr, nc) and not visited[nr][nc] and board[nr][nc]:
                visited[nr][nc] = True
                queue.append((nr, nc, cnt + 1))

    return -1


def solve(board):
    return bfs(0, 0, board)


def main():
    global N, M
    N, M = map(int, input().split())
    board = [list(map(int, input())) for _ in range(N)]

    print(solve(board))


if __name__ == "__main__":
    main()