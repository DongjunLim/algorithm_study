import sys
sys.stdin = open("input.txt","r")

T = int(input())

def dfs(idx, depth):
    global people, answer
    if depth == 1:
        answer += 1

    now = people[idx]

    if now == []:
        return

    for next in now:
        if not visited[next]:
            visited[next] = True
            dfs(next, depth+1)
    return


for tc in range(1,T+1):
    answer = 0
    N ,M = map(int, input().split())
    people = [[] for _ in range(N+1)]
    visited = [False] * (N+1)

    ipt = list(map(int,input().split()))

    for i in range(0,len(ipt)-1,2):
        v1 = ipt[i]
        v2 = ipt[i+1]
        people[v1].append(v2)
        people[v2].append(v1)

    for i in range(1,len(people)):
        if not visited[i]:
            visited[i] = True
            dfs(i,1)

    print(f'#{tc} {answer}')
