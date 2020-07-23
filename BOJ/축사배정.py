import sys
sys.stdin = open("input.txt", "r")
MAX = 1001
visited = []
d = [-1] * MAX


def dfs(idx, cows):
    global visited, d
    for i in range(len(cows[idx])):
        t = cows[idx][i]

        if visited[t]:
            continue

        visited[t] = True
        if d[t] == -1 or dfs(d[t], cows):
            d[t] = idx
            return 1

    return 0


def solve(cows):
    global visited, d, MAX
    cnt = 0

    for i in range(len(cows)):
        visited = [False] * MAX
        cnt += dfs(i, cows)
        visited = [False] * MAX
        cnt += dfs(i, cows)

    return cnt


def main():

    N, M = map(int, input().split())

    cows = [[]*N for _ in range(N)]

    for i in range(N):
        si = list(map(int, input().split()))
        if si[0] != 0:
            cows[i] = si[1:]

    print(solve(cows))


if __name__ == '__main__':
    main()