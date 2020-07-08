import sys
sys.stdin = open("input.txt", "r")


def bst(numbers, target):
    left, right = 0, len(numbers)-1
    if target > numbers[right] or numbers[left] > target:
        return False

    while left <= right:
        mid = (left + right) // 2

        if target is numbers[mid]:
            return True
        if target < numbers[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return False



def solution(numbers, questions):
    for q in questions:
        print("YES") if bst(numbers, q) else print("NO")


def main():
    n, q = map(int, input().split())
    numbers = list(map(int, input().split()))
    questions = list(map(int, input().split()))

    solution(numbers, questions)


if __name__ == "__main__":
    main()