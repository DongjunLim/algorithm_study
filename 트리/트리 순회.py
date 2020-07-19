import sys
sys.stdin = open("input.txt", "r")


def solution(nodes):
    pass


def main():
    N = int(input())
    nodes = [list(input().split()) for _ in range(N)]
    print(nodes)
    solution(nodes)


if __name__ == '__main__':
    main()