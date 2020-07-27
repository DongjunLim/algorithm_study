def solution(name):
    name = list(name)
    for i in range(len(name)):
        name[i] = min(ord(name[i]) - ord('A'), 26 - (ord(name[i]) - ord('A')))

    movement1 = 0
    cnt = 0
    for x in name:
        if x == 0:
            cnt += 1
            continue
        movement1 = movement1 + x + cnt
        cnt = 1

    movement2 = name[0]
    cnt = 1
    for i in range(len(name) - 1, 0, -1):
        if name[i] == 0:
            cnt += 1
            continue
        movement2 = movement2 + name[i] + cnt
        cnt = 1

    cnt = 1
    ACnt = 0
    total = 0
    AIdx = []
    for i in range(1, len(name)):
        if name[i] == 0:
            if ACnt != 0:
                ACnt += 1
                continue
            else:
                ACnt = 1
        else:
            if ACnt > total:
                total = ACnt
                AIdx = [i - ACnt, i - 1]
            ACnt = 0

    idx = 0
    direction = 1
    movement3 = -1
    if AIdx:
        while True:
            if idx >= len(name) or -idx >= len(name):
                break
            if idx == AIdx[0]:
                direction = -1
                idx += direction
                continue

            if len(name) + idx == AIdx[1]:
                break

            movement3 = movement3 + name[idx] + 1
            name[idx] = 0
            idx += direction

            if cnt == len(name):
                break

    answer = min(movement1, movement2)
    if movement3 > -1:
        answer = min(answer, movement3-1)

    return answer

print(solution("ZZAAAAAAAAAAAAAAAAAAAZZ"))