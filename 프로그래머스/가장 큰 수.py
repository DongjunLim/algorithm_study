def compare(x, y):

    xy = str(x) + str(y)
    yx = str(y) + str(x)

    return x if xy > yx else y


def partition(start, mid, end, numbers):
    temp = []
    i, j, k = start, mid, end
    while i < mid and j <= end:
        if compare(numbers[i], numbers[j]) == numbers[i]:
            temp.append(numbers[i])
            i += 1
        else:
            temp.append(numbers[j])
            j += 1
    while i < mid:
        temp.append(numbers[i])
        i += 1
    while j <= end:
        temp.append(numbers[j])
        j += 1

    numbers[start:end+1] = temp

    return


def merge_sort(start, end, numbers):
    if end <= start:
        return

    mid = (start + end) // 2

    merge_sort(start, mid, numbers)
    merge_sort(mid + 1, end, numbers)
    partition(start, mid + 1, end, numbers)

    return


def solution(numbers):

    start = 0
    end = len(numbers) - 1

    merge_sort(start, end, numbers)

    answer = ''.join([str(n) for n in numbers])
    return str(int(answer))


def main():
    numbers = [998, 9, 992]
    print(solution(numbers))
    numbers = [1, 112]
    print(solution(numbers))


if __name__ == '__main__':
    main()