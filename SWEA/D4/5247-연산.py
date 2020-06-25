import sys
from collections import deque
sys.stdin = open("input.txt","r")

T = int(input())
INF = 1000001

for tc in range(1,T+1):
    answer = 0
    cnt = 0
    N, M = map(int,input().split())
    visited = [False] * min(M*2,INF)

    q = deque()
    q.append((N,0))


    visited[N] = True

    while q != []:
        cnt += 1
        now = q.popleft()
        if now[0] == M:
            break

        subOne = now[0]-1
        subTen = now[0]-10
        mulTwo = now[0]*2
        addOne = now[0]+1

        nextCnt = now[1]+1

        if M < now[0]:
            if subOne > 0 and not visited[subOne]:
                visited[subOne] = True
                q.append((subOne, nextCnt))

            if subTen > 0 and not visited[subTen]:
                visited[subTen] = True
                q.append((subTen, nextCnt))
            continue

        if mulTwo <= INF and not visited[mulTwo]:
            visited[mulTwo] = True
            q.append((mulTwo, nextCnt))

        if addOne <= M and not visited[addOne]:
            visited[addOne] = True
            q.append((addOne, nextCnt))

        if subOne > 0 and not visited[subOne]:
            visited[subOne] = True
            q.append((subOne, nextCnt))

        if subTen > 0 and not visited[subTen]:
            visited[subTen] = True
            q.append((subTen, nextCnt))


    answer = now[1]

    print(f'#{tc} {answer}, count: {cnt}')