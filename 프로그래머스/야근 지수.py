import heapq


def solution(n, works):
    max_heap = []
    answer = 0
    for x in works:
        heapq.heappush(max_heap, (-x, x))

    while n:
        now = heapq.heappop(max_heap)[1]
        comparison = max_heap[0][1]

        if now is 0:
            return 0

        sub = now - comparison
        if sub is 0:
            n -= 1
            now -= 1
        elif sub <= n:
            now -= sub
            n -= sub
        else:
            now -= n
            n = 0

        heapq.heappush(max_heap, (-now, now))

    for x in max_heap:
        answer += x[1]**2

    return answer


def main():
    work = [4, 3, 3]
    n = 4
    print(solution(n, work))


if __name__ == '__main__':
    main()