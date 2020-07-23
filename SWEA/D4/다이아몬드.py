from collections import deque
import sys
sys.stdin = open("input.txt", "r")


def solve(n, k, diamonds):

    diamonds.sort()
    queue = deque()
    answer = 0

    for d in diamonds:
        if not queue:
            queue.append(d)
            continue

        if d - k > queue[0]:
            answer = max(answer, len(queue))
            queue = deque()
            continue
        else:
            queue.append(d)

    if queue:
        answer = max(answer, len(queue))

    return answer


def main():
    T = int(input())

    for tc in range(1, T+1):
        N, K = map(int, input().split())
        diamonds = [int(input()) for _ in range(N)]
        print(f'#{tc} {solve(N, K, diamonds)}')


if __name__ == '__main__':
    main()