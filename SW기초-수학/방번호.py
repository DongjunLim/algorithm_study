
def solution(n):
    plasticSet = [0] * 10

    for number in n:
        if number == '6' or number == '9':
            if plasticSet[6] > plasticSet[9]:
                plasticSet[9] += 1
            else:
                plasticSet[6] += 1
        else:
            plasticSet[int(number)] += 1

    return max(plasticSet)


def main():
    N = input()
    print(solution(N))


if __name__ == '__main__':
    main()