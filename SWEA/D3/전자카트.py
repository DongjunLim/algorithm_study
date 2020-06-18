import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

def dfs(idx,depth,total):
    global graph,array, DP,N,answer,isBack
    if depth == N:
        answer.append(graph[idx-1][0] + total)
        return

    now = array[idx]

    for x in now:
        next = x[0]
        value = x[1]
        if not DP[next]:
            DP[next] = True
            dfs(next,depth+1,total+value)
            DP[next] = False

    return

T = int(input())

for tc in range(1,T+1):
    answer = []
    N = int(input())
    isBack = False
    DP = [False] * (N+1)
    graph = [list(map(int,input().split())) for _ in range(N)]

    array = [[] for _ in range(N+1)]

    for i in range(N):
        for j in range(N):
            if i == j: continue
            array[i+1].append((j+1,graph[i][j]))

    DP[1] = True
    dfs(1,1,0)
    print(f'#{tc} {min(answer)}')