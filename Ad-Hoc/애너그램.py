import sys
sys.stdin = open("input.txt", "r")

aCODE = 97


def solution(words):
    global aCODE
    firstWord, secondWord = words
    alphabetCnt = [0] * 100

    for alphabet in secondWord:
        idx = ord(alphabet) - aCODE
        alphabetCnt[idx] += 1

    for alphabet in firstWord:
        idx = ord(alphabet) - aCODE
        alphabetCnt[idx] -= 1
        if alphabetCnt[idx] < 0:
            print(firstWord, "&", secondWord, "are NOT anagrams.")
            return

    print(firstWord, "&", secondWord, "are anagrams.")


def main():
    global alphabets
    T = int(input())

    for tc in range(1, T+1):
        solution(list(input().split()))


if __name__ == '__main__':
    main()