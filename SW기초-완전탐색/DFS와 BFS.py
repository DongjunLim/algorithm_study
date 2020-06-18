import sys
sys.stdin = open("input.txt","r")

def dfs(idx):
    global visited, edgeList, answer
    if visited[idx]:
        return

    visited[idx] = True
    answer.append(str(idx))
    for x in edgeList[idx]:
        dfs(x)


def bfs(idx):
    global visited, edgeList, answer
    s = []
    s.append(idx)
    answer.append(str(idx))
    visited[idx] = True
    while s != []:
        now = s.pop(0)

        for x in edgeList[now]:
            if not visited[x]:
                answer.append(str(x))
                visited[x] = True
                s.append(x)
    return


N, M, V = map(int,input().split())

answer = []
visited = [False] * (N+1)
edgeList = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int,input().split())
    edgeList[a].append(b)
    edgeList[b].append(a)

for x in edgeList:
    x.sort()


dfs(V)
temp = ' '.join(answer)
print(temp)

answer = []
visited = [False] * (N+1)
bfs(V)
temp = ' '.join(answer)
print(temp)