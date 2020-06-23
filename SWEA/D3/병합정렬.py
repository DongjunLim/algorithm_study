import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

T = int(input())
answer = 0
def partition(start,mid,end,all):
    global answer

    if all[mid-1] > all[end]:
        answer += 1
    temp = []
    i , j = start,mid

    while i < mid and j <= end:
        if all[i] < all[j]:
            temp.append(all[i])
            i += 1
            continue
        else:
            temp.append(all[j])
            j += 1
            continue

    while i < mid:
        temp.append(all[i])
        i += 1
    while j <= end:
        temp.append(all[j])
        j += 1

    idx = start
    for x in temp:
        all[idx] = x
        idx += 1




def mergeSort(start,end, all):
    if start >= end:
        return


    mid = (start + end)//2
    mergeSort(start,mid-1, all)
    mergeSort(mid,end-1, all)
    partition(start,mid,end-1,all)






for tc in range(1,T+1):
    answer = 0
    N = int(input())
    numbers = list(map(int,input().split()))
    end = len(numbers)
    mergeSort(0,end,numbers)
    print(f'#{tc} {numbers[N//2]} {answer}')
    print(numbers)
