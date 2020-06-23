import sys
import time
import copy
sys.stdin = open("input.txt","r")

T = int(input())

def quickSort(a,left,right):
    arr = a
    if left >= right:
        return

    i , j = left, right
    p = arr[right]

    while i <= j:
        while arr[i] < p: i+=1
        while arr[j] > p: j-=1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    quickSort(arr,left,j)
    quickSort(arr,i,right)


for tc in range(1,T+1):
    N = int(input())
    array = list(map(int,input().split()))
    array2 = copy.deepcopy(array)
    print(f"길이: {len(array)}")
    start = time.time()
    quickSort(array,0,len(array)-1)
    ms = (time.time()-start) * 1000
    print(f'시간: {round(ms,2)}ms')

    start = time.time()
    array2.sort()
    ms = (time.time()-start) * 1000
    print(f'시간: {round(ms,2)}ms')
