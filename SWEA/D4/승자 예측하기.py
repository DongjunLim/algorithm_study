import sys
sys.stdin = open("input.txt", "r")


def back_tracking(x, n, who, players):
    global winner
    if n < x:
        winner = players[(who+1) % 2]
        return

    back_tracking(2*x, n, 1, players)
    back_tracking(2*x+1, n, 1, players)

    pass


def solution(n):
    players = ['Alice','Bob']

    if n is 1:
        return 'Bob'
    if n < 4:
        return 'Alice'


def main():
    T = int(input())

    for tc in range(1, T+1):
        N = int(input())
        print(f'#{tc} {solution(N)}')

    return


if __name__ == "__main__":
    main()