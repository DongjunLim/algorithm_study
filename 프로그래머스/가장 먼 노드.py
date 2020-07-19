from collections import deque


def set_adj_list(n, edge):

    adj_list = [[] for _ in range(n+1)]

    for u, v in edge:
        adj_list[u].append(v)
        adj_list[v].append(u)

    return adj_list


def solution(n, edge):
    adj_list = set_adj_list(n, edge)

    queue = deque()

    visited = [False] * (n + 1)
    visited[1] = True

    for x in adj_list[1]:
        queue.append([x, 1])
        visited[x] = True

    maxDepth = 0
    depthCnt = 1
    while queue:
        now = queue.popleft()
        node = now[0]
        depth = now[1]

        if depth > maxDepth:
            maxDepth = depth
            depthCnt = 1
        elif depth == maxDepth:
            depthCnt += 1

        for x in adj_list[node]:
            if not visited[x]:
                visited[x] = True
                queue.append([x, depth + 1])

    return depthCnt


def main():
    vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    n = 6

    print(solution(n, vertex))

if __name__ == '__main__':
    main()