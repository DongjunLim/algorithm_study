def solution(row, col, r, c, startRow, startCol, nowFirstVal):

    size = (row * col) // 4
    if size < 4:
        print(row, col, startRow, startCol, r, c)
        return

    first = [startRow, startCol]
    second = [startRow, startCol + (size//4)]
    third = [startRow + (size//4), startCol]
    fourth = [startRow + (size//4), startCol + (size//4)]


    firstVal = nowFirstVal


    secondVal = firstVal + size
    thirdVal = secondVal + size
    fourthVal = thirdVal + size

    print(first, second, third, fourth)
    print(firstVal, secondVal, thirdVal, fourthVal)

    if r < third[0] and c < second[1]:
        solution(row//2, col//2, r, c, first[0], first[1], nowFirstVal)

    elif r < third[0] and second[1] <= c:
        solution(row//2, col//2, r, c, second[0], second[1], secondVal)

    elif third[0] <= r and c < second[1]:
        solution(row//2, col//2, r, c, third[0], third[1], thirdVal)

    elif third[0] <= r and second[1] <= c:
        solution(row//2, col//2, r, c, fourth[0], fourth[1], fourthVal)






def main():
    N, r, c = map(int, input().split())

    solution(2**N, 2**N, r, c, 0, 0, 0)


if __name__ == '__main__':
    main()