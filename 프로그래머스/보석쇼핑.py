from collections import deque

INF = 9999999999


def add_gem(gems, gemHash, idx):
    if gems[idx] not in gemHash.keys() or gemHash[gems[idx]] == 0:
        gemHash[gems[idx]] = 1
        return 1
    else:
        gemHash[gems[idx]] += 1
        return 0


def solution(gems):
    global INF
    answer = []
    i, j = 0, 0
    temp = INF
    totalCnt = len(set(gems))
    gemHash = dict()
    cnt = 0

    while i < len(gems):
        while j < len(gems) + 1:
            if cnt == totalCnt:
                rg = j-i
                if rg < temp:
                    temp = rg
                    answer = [i+1, j]

                gemHash[gems[i]] -= 1
                if gemHash[gems[i]] == 0:
                    cnt -= 1
                break

            if len(gems) == j:
                break
            cnt += add_gem(gems, gemHash, j)
            j += 1

        i += 1

    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))