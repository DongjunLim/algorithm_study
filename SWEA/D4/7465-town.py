import sys
sys.stdin = open("../D4/input.txt", "r")

T = int(input())

for tc in range(1,T + 1):
    N, M = map(int, input().split())
    people = []

    #사람이 어느 그룹인지 인덱스 확인하는
    whereGroup = [-1 for i in range(N+1)]
    groupList = [[i] for i in range(N+1)]
    count = 0

    for i in range(M):
        people.append(list(map(int,input().split())))



    for x in people:

        if whereGroup[x[1]] == -1:
            if whereGroup[x[0]] != -1:
                groupList[whereGroup[x[0]]].append(x[1])
                whereGroup[x[1]] = whereGroup[x[0]]
                groupList[x[1]] = []
            else:
                groupList[x[0]].append(x[1])
                whereGroup[x[1]] = x[0]
                whereGroup[x[0]] = x[0]
                groupList[x[1]] = []
        elif whereGroup[x[0]] == -1:
            groupList[whereGroup[x[1]]].append(x[0])
            whereGroup[x[0]] = whereGroup[x[1]]
            groupList[x[0]] = []

        elif whereGroup[x[0]] != whereGroup[x[1]]:
            groupList[whereGroup[x[0]]] =groupList[whereGroup[x[0]]] + (groupList[whereGroup[x[1]]])
            groupList[whereGroup[x[1]]] = []
    for x in groupList[1:]:
        if len(x) != 0:
            count = count + 1

    print(f'#{tc} {count}')