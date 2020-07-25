import sys

sys.stdin = open("input.txt", "r")

INF = 10000000000000000017


def solve(n, pole):
    global MAX
    answer = None
    left, right = 0, INF

    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        temp = pole.copy()
        for i in range(1, len(temp)):
            if temp[i] - mid != temp[i - 1]:
                cnt += abs(temp[i] - (temp[i - 1] + mid))
                temp[i] = temp[i - 1] + mid

        if answer is None or cnt < answer:
            answer = cnt
            right = mid - 1
        else:
            left = mid + 1

    return answer


def main():
    N = int(input())
    pole = list(map(int, input().split()))

    print(solve(N, pole))


if __name__ == "__main__":
    main()
