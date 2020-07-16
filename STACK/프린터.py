"""
    Queue를 사용해 풀었습니다.
    우선순위가 낮을경우 인덱스 값이 계속 변하기 때문에
    인덱스 위치를 저장할 idxQ 를 생성해 value가 뒤로 밀리면
    인덱스 값도 뒤로 밀리게 설계했습니다.
"""

from collections import deque


def solution(priorities, location):
    answer = 0

    queue = deque(priorities)
    idxQ = deque([i for i in range(len(queue))])

    while len(queue) > 1:
        now = queue.popleft()
        idx = idxQ.popleft()

        if now >= max(queue):
            answer += 1
            if idx is location:
                return answer
        else:
            queue.append(now)
            idxQ.append(idx)

    return answer + 1