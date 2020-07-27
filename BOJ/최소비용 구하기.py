import sys
import heapq
sys.stdin = open("input.txt", "r")
n, m = 0, 0
INF = 999999999999


def dijkstra(start, end, adj_list):
    global n, m
    answer = 0
    queue = []
    dist = [INF] * (n + 1)

    for edge in adj_list[start]:
        if dist[edge[1]] > edge[0]:
            dist[edge[1]] = edge[0]
        heapq.heappush(queue, edge)

    dist[start] = 0

    while queue:
        w, nn = heapq.heappop(queue)

        if nn == end:
            return dist[end]

        for nw, node in adj_list[nn]:
            if dist[node] > nw + w:
                dist[node] = nw + w
                heapq.heappush(queue, [w+nw, node])

    return answer


def solve(start, end, adj_list):

    return dijkstra(start, end, adj_list)


def main():
    global n, m
    n = int(input())
    m = int(input())

    adj_list = [[] for _ in range(n+1)]
    for _ in range(m):
        edge = list(map(int, input().split()))
        adj_list[edge[0]].append([edge[2], edge[1]])

    start, end = map(int, input().split())

    print(solve(start, end, adj_list))


if __name__ == "__main__":
    main()