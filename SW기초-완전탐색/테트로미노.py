import sys

def maxSumI(posX, posY):
    global tMap, N, M
    sumList = []
    if posY + 3 < M:
        sumList.append(sum(tMap[posX][posY:posY+4]))
    if posX + 3 < N:
        sumList.append(sum([tMap[i][posY] for i in range(posX,posX+4)]))
    if sumList != []:
        return max(sumList)
    return 0

def maxSumO(posX, posY):
    global tMap, N, M
    if posX + 1 < N and posY + 1 < M:
        return sum(tMap[posX][posY:posY+2])+tMap[posX+1][posY]+tMap[posX+1][posY+1]

    return 0

def maxSumT(posX, posY):
    global tMap, N, M
    sumList = []
    if posX + 1 < N and posY + 2 < M:
        sumList.append(sum(tMap[posX][posY:posY+3])+tMap[posX+1][posY+1])
    if posX + 2 < N and posY - 1 > -1:
        sumList.append(sum([tMap[i][posY] for i in range(posX,posX+3)]) + tMap[posX+1][posY-1])
    if posX -1 > -1 and posY - 2 > -1:
        sumList.append(sum(tMap[posX][posY-2:posY+1])+tMap[posX-1][posY-1])
    if posX - 2 > -1 and posY + 1 < M:
        sumList.append(sum([tMap[i][posY] for i in range(posX-2,posX+1)]) + tMap[posX-1][posY+1])

    if sumList != []:
        return max(sumList)

    return 0

def maxSumJ(posX, posY):
    global tMap, N, M
    sumList = []
    if posX + 1 < N and posY + 2 < M:
        sumList.append(sum(tMap[posX][posY:posY+3])+tMap[posX+1][posY])
    if posX + 2 < N and posY -1 > -1:
        sumList.append(sum([tMap[i][posY] for i in range(posX,posX+3)]) + tMap[posX][posY-1])
    if posX -1 > -1 and posY -2 > -1:
        sumList.append(sum(tMap[posX][posY-2:posY+1]) + tMap[posX-1][posY])
    if posX -2 > -1 and posY + 1 < M:
        sumList.append(sum([tMap[i][posY] for i in range(posX-2,posX+1)]) + tMap[posX][posY+1])

    if sumList != []:
        return max(sumList)
    return 0

def maxSumL(posX, posY):
    global tMap, N, M
    sumList = []
    if posX -1 > -1 and posY + 2 < M:
        sumList.append(sum(tMap[posX][posY:posY+3]) + tMap[posX-1][posY])
    if posX + 2 < N and posY + 1 < M:
        sumList.append(sum([tMap[i][posY] for i in range(posX,posX+3)]) + tMap[posX][posY+1])
    if posX + 1 < N and posY -2 > -1:
        sumList.append(sum(tMap[posX][posY-2:posY+1]) + tMap[posX+1][posY])
    if posX - 2 > -1 and posY -1 > -1:
        sumList.append(sum([tMap[i][posY] for i in range(posX-2,posX+1)]) + tMap[posX][posY-1])

    if sumList != []:
        return max(sumList)
    return 0

def maxSumS(posX, posY):
    global tMap, N, M
    sumList = []
    if posX + 2 < N and posY + 1 < M:
        sumList.append(tMap[posX][posY] + tMap[posX+1][posY] + tMap[posX+1][posY+1] + tMap[posX+2][posY+1])
    if posX + 1 < N and posY -2 > -1:
        sumList.append(tMap[posX][posY] + tMap[posX][posY-1] + tMap[posX+1][posY-1] + tMap[posX+1][posY-2])
    if posX - 2 > -1 and posY -1 > -1:
        sumList.append(tMap[posX][posY] + tMap[posX-1][posY] + tMap[posX-1][posY-1] + tMap[posX-2][posY-1])
    if posX - 1 > -1 and posY + 2 < M:
        sumList.append(tMap[posX][posY] + tMap[posX][posY+1] + tMap[posX-1][posY+1] + tMap[posX-1][posY+2])

    if sumList != []:
        return max(sumList)
    return 0


def maxSumZ(posX, posY):
    global tMap, N, M
    sumList = []
    if posX + 2 < N and posY - 1 > -1:
        sumList.append(tMap[posX][posY] + tMap[posX + 1][posY] + tMap[posX + 1][posY - 1] + tMap[posX + 2][posY - 1])
    if posX - 1 > -1 and posY - 2 > -1:
        sumList.append(tMap[posX][posY] + tMap[posX][posY - 1] + tMap[posX - 1][posY - 1] + tMap[posX - 1][posY - 2])
    if posX - 2 > -1 and posY + 1 < M:
        sumList.append(tMap[posX][posY] + tMap[posX - 1][posY] + tMap[posX - 1][posY + 1] + tMap[posX - 2][posY + 1])
    if posX + 1 < N and posY + 2 < M:
        sumList.append(tMap[posX][posY] + tMap[posX][posY + 1] + tMap[posX + 1][posY + 1] + tMap[posX + 1][posY + 2])

    if sumList != []:
        return max(sumList)
    return 0


arr = [maxSumI,maxSumO,maxSumT,maxSumJ,maxSumL,maxSumS,maxSumZ]

sys.stdin = open("input.txt","r")

N, M = map(int,input().split())

tMap = [list(map(int, input().split())) for _ in range(N)]
candidates = []
for i in range(N):
    for j in range(M):
        for x in arr:
            candidates.append(x(i,j))

print(max(candidates))