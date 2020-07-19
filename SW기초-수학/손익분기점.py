
def solution(a, b, c):
    profit = c - b

    if profit < 1:
        return -1

    return (a // profit) + 1


def main():
    A, B, C = map(int, input().split())
    print(solution(A, B, C))


if __name__ == '__main__':
    main()