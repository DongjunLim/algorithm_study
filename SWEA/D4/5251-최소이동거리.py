import heapq
from collections import deque
import sys
sys.stdin = open("input.txt","r")
INF = 9999999999
T = int(input())


for tc in range(1,T+1):
    N, E = map(int, input().split())

    graph = [[] for _ in range(N+1)]
    graph = deque(graph)
    queue = deque()
    for i in range(E):
        v1, v2, w = map(int, input().split())
        graph[v1].append((w,v1,v2))

    dist = [INF] * (N+1)
    start = 0
    dist[start] = 0

    for x in graph[0]:
        queue.append(x)

    while queue:
        now = queue.popleft()
        cost = now[0]
        u = now[1]
        v = now[2]

        if dist[v] < dist[u] + cost:
            continue

        dist[v] = dist[u] + cost

        for x in graph[v]:
            queue.append(x)

    print(f'#{tc} {dist[N]}')
