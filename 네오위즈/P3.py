import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

T = int(input())

for tc in range(1,T+1):
    array = list(map(int,input().split()))
    array.sort()
    temp = []
    idx = 1
    answer = 0
    while True:
        if idx == len(array):
            break
        if array[idx-1] == array[idx]:
            array.append(array[idx])
            del array[idx]
            continue
        elif array[idx-1] < array[idx]: answer += 1
        idx += 1

    # n = len(array)
    # for i in range(1,n):
    #     if array[i-1] == array[i]:
    #         temp.append(array[i])
    #         n -= 1
    # array = list(set(array))
    #
    # idx = 0
    # while temp != []:





