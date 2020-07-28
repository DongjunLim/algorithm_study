from collections import deque


def solution(number, k):
    stack = deque()

    stack.append(number[0])
    idx = 1
    while idx < len(number):

        while stack and k and stack[-1] < number[idx]:
            stack.pop()
            k -= 1
            if k == 0:
                break

        stack.append(number[idx])
        idx += 1

    answer = ''.join(stack)

    return answer[:len(answer)-k]