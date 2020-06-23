import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())

    products = [tuple(map(int,input().split())) for _ in range(M)]
    K = [[0] * (N + 1) for _ in range(M + 1)]
    w = M
    for i in range(1,M+1):
        for j in range(1,N+1):
            if j >= products[i-1][0]:
                K[i][j] = max(K[i-1][j],K[i-1][j-products[i-1][0]] + products[i-1][1])
            else:
                K[i][j] = K[i-1][j]

    for x in K:
        print(x)
    print(K[M][N])
