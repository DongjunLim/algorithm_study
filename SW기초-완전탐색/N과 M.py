import sys
sys.stdin = open("input.txt", "r")

visited = []
dp = set()


def is_overlap(number):
    global dp

    val = ''
    i = 1
    for x in number:
        val += str(x)
        val += '-'

    if val in dp:
        return True

    dp.add(val)

    return False


def print_number(number):
    for x in number[:-1]:
        print(x, end=' ')
    print(number[-1])
    return


def dfs(idx, number, n, m, numbers):
    global visited, dp
    if len(number) > m:
        return

    if len(number) == m and not is_overlap(number):
        print_number(number)
        return

    for i in range(len(numbers)):
        if not number or number[-1] <= numbers[i]:
            number.append(numbers[i])
            dfs(idx + 1, number, n, m, numbers)
            number.pop()


def solve(n, m, numbers):
    global visited, dp
    visited = [False] * 10001
    numbers.sort()

    return dfs(0, [], n, m, numbers)


def main():
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))

    solve(n, m, numbers)


if __name__ == '__main__':
    main()
