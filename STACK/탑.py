import sys
from collections import deque
sys.stdin = open("input.txt", "r")

def solution():

    n = int(input())
    tops = list(map(int, input().split()))

    stack = deque()
    answer = [0] * n
    for i, top in enumerate(tops):
        while stack:
            if top > stack[-1][1]:
                stack.pop()
            else:
                break
        if not stack:
            answer[i] = '0'
        else:
            answer[i] = str(stack[-1][0])

        stack.append([i+1, top])

    print(' '.join(answer))





def main():

    solution()

if __name__ == "__main__":
    main()