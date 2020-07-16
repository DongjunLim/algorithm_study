"""
    Stack을 사용해 풀었습니다.
    레이저가 나올경우 누적된 쇠막대기의 합만큼 answer에 더합니다.
    레이저가 아닐 때 ( 가 나오면 스택에 push 하고,
    ) 가 나오면 스택에서 pop을 해서 막대기를 빼줍니다.
"""

from collections import deque


def razer(sticks):
    sticks.pop()
    return len(sticks)


def end_stick(sticks):
    sticks.pop()
    return 1


def add_stick(sticks, x):
    sticks.append(x)
    return 0


def process(idx, value, sticks, arrangement):
    if value is ')' and arrangement[idx - 1] is '(':
        return razer(sticks)

    if value is ')':
        return end_stick(sticks)

    return add_stick(sticks, value)


def solution(arrangement):
    answer = 0
    sticks = deque()

    for i, x in enumerate(arrangement):
        answer += process(i, x, sticks, arrangement)

    return answer