
'''
문제
1. n * n 크기의 격자에 1~9까지의 정수가 입력된 리스트를 받음
2. 왼쪽 위칸에서 시작해 오른쪽 아래칸에 도착할 수 있는지 없는지 확인하는 문제
3. 이동은 격자에 쓰여져 있는 숫자만큼 이동 가능

아이디어
1. 움직이는건 우,하
2. 우측하단 도착지 옆 인덱스부터 차례로 이동좌표가 True인지 검사
3. True면 검사인덱스도 True로 변환
4. 최종적으로 [0][0] 인덱스 값이 True면 길이 있는거고 False면 없는거

'''

#메모이제이션
cache = [[False for i in range(19)] for j in range(19)]

#인풋데이터
gameMap = [
    [2,5,1,6,1,4,1],
    [6, 1, 1, 2, 2, 9, 3],
    [7, 2, 3, 2, 1, 3, 1],
    [2, 1, 3, 1, 7, 1, 2],
    [5, 1, 2, 3, 4, 1, 2],
    [4, 3, 1, 2, 3, 4, 1],
    [2, 5, 2, 9, 4, 3, 0],
]

#반복동적계획
def solution(n):
    goal = len(n)-1
    cache[goal][goal] = True
    x = goal
    y = goal -1
    while True:
        while True:
            if cache[x][y+n[x][y]] is True:
                cache[x][y] = True
            elif cache[x+n[x][y]][y] is True:
                cache[x][y] = True

            if y==0:
                y=goal
                break
            else:
                y = y-1
        if x==0:
            break
        else:
            x = x-1
    return cache[0][0]


print(solution(gameMap))
