import sys
from collections import deque
INF = 1000001
sys.stdin = open("input.txt", "r")


def bfs(f, s, g, u, d):
    global INF
    visited = [False] * INF
    queue = deque()

    queue.append((s, 0))
    visited[s] = True
    while queue:
        now, cnt = queue.popleft()

        if now == g:
            return cnt

        if now+u < INF and not visited[now+u]:
            queue.append((now+u, cnt + 1))
            visited[now+u] = True

        if now-d > 0 and not visited[now-d]:
            queue.append((now-d, cnt + 1))
            visited[now-d] = True

    return "use the stairs"


def solve(f, s, g, u, d):

    return bfs(f, s, g, u, d)


def main():
    F, S, G, U, D = map(int, input().split())

    print(solve(F, S, G, U, D))


if __name__ == '__main__':
    main()