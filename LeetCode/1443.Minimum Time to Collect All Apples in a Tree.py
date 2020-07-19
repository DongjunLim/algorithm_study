def set_adj_list(n, edges):

    adj_list = [[] for _ in range(n)]

    for u, v in edges:
        adj_list[u].append(v)

    return adj_list


def dfs(now, moveCnt, adj_list, visited, hasApple):

    visited[now] = True
    nowCnt = moveCnt

    if adj_list[now] == []:
        if hasApple[now]:
            return nowCnt
        return nowCnt - 2


    for next in adj_list[now]:
        if not visited[next]:
            nowCnt = dfs(next, nowCnt + 2, adj_list, visited, hasApple)

    if nowCnt > moveCnt:
        return nowCnt
    else:
        if hasApple[now]:
            return nowCnt
        return nowCnt - 2


def solution(n, edges, hasApple):

    adj_list = set_adj_list(n, edges)
    visited = [False] * n

    result = dfs(0, 0, adj_list, visited, hasApple)

    if result < 0:
        return 0

    return result



def main():
    n = 7
    edges = [[0, 1],[0, 2],[1, 4],[1, 5],[2, 3],[2, 6]]
    hasApple = [False, False, True, False, True, True, False]

    print(solution(n, edges, hasApple))

    n = 7
    edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
    hasApple = [False, False, True, False, False, True, False]

    print(solution(n, edges, hasApple))

    n = 7
    edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
    hasApple = [False, False, False, False, False, False, False]

    print(solution(n, edges, hasApple))

    n = 4
    edges = [[0,1],[0,2],[0,3]]
    hasApple = [True, True, True, True]

    print(solution(n, edges, hasApple))

    n = 4
    edges = [[0,1],[0,2],[0,3]]
    hasApple = [True, True, True, True]

    print(solution(n, edges, hasApple))

    n = 6
    edges = [[0, 1], [0, 2], [1, 3], [3, 4], [4, 5]]
    hasApple = [False, True, False, False, True, True]

    print(solution(n, edges, hasApple))

if __name__ == "__main__":
    main()
