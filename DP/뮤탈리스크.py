import sys
from collections import deque
sys.stdin = open("input.txt", "r")

damages = [9, 3, 1]
answer = 999999999

def dfs():
    global damages, answer


def solution(n, scvs):
    finished = [False] * n
    scvs.append(0)
    queue = deque()
    queue.append(scvs)
    depth = 0
    temp = n
    while queue:
        now = queue.pop()

        for i in range(temp):
            if not finished[i] and now[i] <= 0:
                finished[i] = True

        if finished.count(True) == n:
            return now[-1]
        next = []



    print(answer)


def main():
    n = int(input())
    scvs = list(map(int, input().split()))

    solution(n, scvs)


if __name__ == '__main__':
    main()