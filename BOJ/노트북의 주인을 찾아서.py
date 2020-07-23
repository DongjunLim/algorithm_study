import sys
sys.stdin = open("input.txt", "r")


def dfs(idx, adj_list, d, visited):

    for t in adj_list[idx]:

        if visited[t]:
            continue

        visited[t] = True

        if d[t] == -1 or dfs(d[t], adj_list, d, visited):
            d[t] = idx
            return True

    return False


def solve(n, adj_list):
    d = [-1] * (n+1)
    cnt = 0
    for i in range(1, n+1):
        visited = [False] * (n + 1)

        if dfs(i, adj_list, d, visited):
            cnt += 1

    return cnt


def main():
    N, M = map(int, input().split())

    adj_list = [[] for _ in range(N+1)]

    for i in range(M):
        a, b = map(int, input().split())
        adj_list[a].append(b)

    print(solve(N, adj_list))


if __name__ == "__main__":
    main()