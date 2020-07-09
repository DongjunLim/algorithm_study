import sys
sys.stdin = open("input.txt", "r")


def binary_search(numbers, target):
    left, right = 0, len(numbers)-1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            return mid
        if numbers[mid] < target:
            left = mid + 1
        if numbers[mid] > target:
            right = mid - 1

    return -1


def solution(numbers, questions):





def main():
    n, q = map(int, input().split())

    numbers = list(map(int, input().split()))
    questions = list(map(int, input().split()))
    solution(numbers, questions)


if __name__ == '__main__':
    main()