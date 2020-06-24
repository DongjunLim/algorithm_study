import sys
sys.stdin = open("input.txt","r")

INF = 9999999999
T = int(input())


def dfs(idx,totalCost):
    global N,V, answer
    if answer < totalCost:
        return

    if idx == N:
        answer = totalCost
        return

    nowProduct = products[idx]

    for i,nowCost in enumerate(nowProduct):
        if not factories[i]:
            factories[i] = True
            dfs(idx+1,totalCost+nowCost)
            factories[i] = False



for tc in range(1,T+1):

    answer = INF
    N = int(input())
    products = [list(map(int,input().split())) for _ in range(N)]
    print(products)
    factories = [False] * N
    dfs(0,0)
    print(f'#{tc} {answer}')