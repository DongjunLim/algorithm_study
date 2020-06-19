import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

T = int(input())

for tc in range(1,T+1):
    N = int(input())

    schedules = [tuple(map(int,input().split())) for _ in range(N)]

    schedules.sort(key= lambda element: element[1])

    time = 0
    answer = 0

    for x in schedules:
        start = x[0]
        if time <= start:
            answer += 1
            time = x[1]
            continue


    print(f'#{tc} {answer}')