import heapq


def set_adj_list(n, costs):
    adj_list = [[] for _ in range(n)]

    for u, v, w in costs:
        adj_list[u].append([w, v])
        adj_list[v].append([w, u])

    return adj_list


def solution(n, costs):
    global INF
    adj_list = set_adj_list(n, costs)
    queue = []
    answer = 0

    visited = [False] * n

    for x in adj_list[0]:
        heapq.heappush(queue, x)

    visited[0] = True

    while queue:
        now = heapq.heappop(queue)
        if visited[now[1]]:
            continue

        visited[now[1]] = True
        answer += now[0]

        for x in adj_list[now[1]]:
            if not visited[x[1]]:
                heapq.heappush(queue, x)

    return answer


def main():
    costs = [[0,1,7],[0,3,5],[1,2,8],[1,3,9],[1,4,7], [2,4,5],[3,4,15],[3,5,6],[4,5,8],[4,6,9],[5,6,11]]
    n = 7

    print(solution(n, costs))



if __name__ == '__main__':
    main()