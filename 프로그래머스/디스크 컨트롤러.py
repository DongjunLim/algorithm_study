import heapq
from collections import deque


def solution(jobs):
    maxTime = 501001
    jobs.sort()
    jobs = deque(jobs)
    length = len(jobs)
    ready = []
    running = []
    answer = 0
    for time in range(maxTime):
        while jobs:
            if jobs[0][0] > time:
                break
            elif jobs[0][0] == time:
                heapq.heappush(ready, [jobs[0][1], jobs[0][0]])
                jobs.popleft()

        if not running and not ready:
            if not jobs:
                break
            continue

        if running and running[1] == time:
            answer += running[1] - running[0]
            running = []

        if not running and ready:
            nextJob = heapq.heappop(ready)
            running = [nextJob[1], nextJob[0] + time]

    return answer // length


def main():
    jobs = [[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]
    print(solution(jobs))


if __name__ == '__main__':
    main()