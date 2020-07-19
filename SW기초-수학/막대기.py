def solution(target):
    now = 64
    cnt = 0

    while now > 0:
        if target >= now:
            target -= now
            cnt += 1

        if target == 0:
            return cnt

        now = now // 2

    return cnt + target


def main():
    X = int(input())

    print(solution(X))


if __name__ == '__main__':
    main()