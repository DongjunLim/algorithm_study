import sys
sys.stdin = open("input.txt","r")
T = int(input())

def dfs(x,y,maxSum):
    global visited, board, routeCount, answer, isNumbers, N, M

    if x == N or y == M:
        return

    if x == N-1 and y == M-1:
        routeCount += 1
        answer = max(answer, maxSum)
        return

    if x != N-1:
        right = board[x+1][y]
        if not isNumbers[right] and not visited[x+1][y]:
            isNumbers[right] = True
            visited[x+1][y] = True
            dfs(x+1,y,right + maxSum)
            isNumbers[right] = False
            visited[x+1][y] = False

    if y != M-1:
        down = board[x][y+1]
        if not isNumbers[down] and not visited[x][y+1]:
            isNumbers[down] = True
            visited[x][y+1] = True
            dfs(x, y + 1, down + maxSum)
            isNumbers[down] = False
            visited[x][y+1] = False





for tc in range(1,T+1):
    N, M = map(int,input().split())

    isNumbers = [False]* 201

    board = [list(map(int,input().split())) for _ in range(N)]

    routeCount = 0
    answer = 0

    visited = [[False]*M for _ in range(N)]

    visited[0][0] = True
    isNumbers[board[0][0]] = True

    dfs(0,0,board[0][0])
    if answer == 0:
        answer = -1
    print(f'#{tc} {routeCount} {answer}')

