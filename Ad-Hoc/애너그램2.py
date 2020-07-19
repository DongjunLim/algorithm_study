import sys
sys.stdin = open("input.txt", "r")


def solution(words):
    global aCODE
    firstWord, secondWord = words
    fLength = len(firstWord)
    sLength = len(secondWord)

    if fLength > sLength:
        return f'{firstWord} & {secondWord} are NOT anagrams.'

    f = list(firstWord)
    f.sort()
    s = list(secondWord)
    s.sort()

    if f != s[:fLength]:
        return f'{firstWord} & {secondWord} are NOT anagrams.'

    return f'{firstWord} & {secondWord} are anagrams.'


def main():
    global alphabets
    T = int(input())

    for tc in range(1, T+1):
        print(solution(list(input().split())))


if __name__ == '__main__':
    main()