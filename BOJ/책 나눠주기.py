import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10000)
input = lambda: sys.stdin.readline().strip()
MAX = 1010


def dfs(idx, adj_list, d, visited):

    for t in adj_list[idx]:
        if visited[t]:
            continue
        visited[t] = True

        if d[t] == -1 or dfs(d[t], adj_list, d, visited):
            d[t] = idx
            return True

    return False


def solve(n, m, adj_list):
    global MAX
    d = [-1] * MAX
    cnt = 0

    for i in range(1, m+1):
        visited = [False] * MAX
        if dfs(i, adj_list, d, visited):
            cnt += 1

    return cnt


def main():
    global MAX, input
    T = int(input())

    for tc in range(1, T+1):
        N, M = map(int, input().split())
        adj_list = [[] for _ in range(MAX)]

        for i in range(1, M+1):
            a, b = map(int, input().split())
            for j in range(a, b+1):
                adj_list[i].append(j)

        print(solve(N, M, adj_list))


if __name__ == "__main__":
    main()