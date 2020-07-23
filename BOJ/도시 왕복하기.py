from collections import deque
import sys

sys.stdin = open("input.txt", "r")
INF = 9999999999


def max_flow(start, end, a, c, n, p):
    global INF
    f = [[0] * (n + 1) for _ in range(n + 1)]
    visited= [[False] * (n + 1) for _ in range(n + 1)]
    result = 0

    while True:
        d = [-1] * (n + 1)
        q = deque()
        q.append(start)

        while q:
            x = q.popleft()
            for i in range(len(a[x])):
                y = a[x][i]

                if c[x][y] - f[x][y] > 0 and d[y] == -1:
                    q.append(y)
                    d[y] = x
                    if y == end:
                        break

        if d[end] == -1:
            break
        flow = INF
        i = end
        while i != start:
            flow = min(flow, c[d[i]][i] - f[d[i]][i])
            i = d[i]

        i = end

        while i != start:
            f[d[i]][i] += flow
            f[i][d[i]] -= flow
            i = d[i]

        result += flow

    return result


def main():
    N, P = map(int, input().split())

    a = [[] for _ in range(N + 1)]
    c = [[0] * (N + 1) for _ in range(N + 1)]

    for _ in range(P):
        u, v = map(int, input().split())
        a[u].append(v)
        a[v].append(u)
        c[u][v] = 1
        c[v][u] = 1

    print(max_flow(1, 2, a, c, N, P))


if __name__ == '__main__':
    main()
