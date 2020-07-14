import sys
import heapq
sys.stdin = open("input.txt", "r")

INF = 999999999
def prim(n, m, adj_list):
    visited = [False] * (n+1)
    key = [INF] * (n+1)
    key[0] = 0
    key[1] = 0

    for _ in range(n):

        maxWeight = INF
        nextIdx = -1
        for i in range(1, n+1):
            if key[i] < maxWeight and not visited[i]:
                nextIdx = i
                maxWeight = key[i]

        visited[nextIdx] = True

        for edge in adj_list[nextIdx]:
            if not visited[edge[0]]:
                key[edge[0]] = min(key[edge[0]], edge[1])

    # print(key)
    return sum(key)


def solution(n ,m, edgeList):

    return prim(n, m, edgeList)


def main():
    N = int(input())
    M = int(input())

    edges = [list(map(int, input().split())) for _ in range(M)]
    adj_list = [[] for _ in range(N+1)]
    for x in edges:
        adj_list[x[0]].append((x[1], x[2]))
        adj_list[x[1]].append((x[0], x[2]))

    print(solution(N, M, adj_list))

if __name__ == '__main__':
    main()