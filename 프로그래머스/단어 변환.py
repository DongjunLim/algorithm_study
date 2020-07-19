"""
    BFS 알고리즘을 사용해 풀었습니다.
    먼저 words 배열에 target이 들어 있지 않으면 정답을 구할 수 없으므로 0을 반환합니다.
    begin 문자열이 만약 words에 들어 있지 않으면 words에 begin을 삽입하고
    bfs를 begin부터 시작합니다.
    words에 begin이 들어 있는지 확인하는 이유는, begin이 words에 들어 있을 경우
    bfs 중간에 begin 문자열을 탐색해 꼬일 수 있기 때문입니다.
    따라서 방문처리를 위해 words에 begin이 없을 경우 삽입하고 탐색이 시작될떄 방문처리를 해주어서
    중복 탐색을 방지합니다.
"""

from collections import deque


def is_change(now, x):
    """ 문자열 now와 x가 한글자만 차이나는지 확인. """

    length = len(now)
    cnt = 0
    for i in range(length):
        if now[i] != x[i]:
            cnt += 1
        if cnt > 1:
            return False

    if cnt == 1:
        return True
    else:
        return False


def bfs(begin, target, words):
    """ 넓이 우선 탐색으로 begin에서 target까지의 최소 거리를 구함. """

    length = len(words)
    visited = [False] * length

    queue = deque()
    queue.append((begin, 0, len(words) - 1))

    while queue:
        now, depth, idx = queue.popleft()

        if now == target:
            return depth

        if depth == length:
            continue

        visited[idx] = True

        for i, x in enumerate(words):
            if not visited[i] and is_change(now, x):
                queue.append((x, depth + 1, i))

    return 0


def solution(begin, target, words):

    if target not in words:
        return 0

    if begin not in words:
        words.append(begin)

    return bfs(begin, target, words)


def main():
    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(solution(begin, target, words))
    words = ["hot", "dot", "dog", "lot", "log"]
    print(solution(begin, target, words))


if __name__ == '__main__':
    main()