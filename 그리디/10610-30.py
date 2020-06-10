import sys
sys.stdin = open("input.txt","r")

def solution():
    # 테스트케이스 입력받음
    N = str(input())

    # 1~9까지 숫자갯수를 담을 리스트
    arr = [0 for _ in range(10)]

    # 숫자들의 합을 담을 변수
    Sum = 0

    for x in N:
        Sum += int(x)
        arr[int(x)] += 1

    answer = ''

    # 숫자의 합이 3으로 나눠지지 않거나 입력데이터 0이 없으면 30의 배수가 아님
    # 따라서 -1을 출력
    if Sum % 3 != 0 or arr[0] == 0:
        return -1

    # 30의 배수일 경우 숫자 9부터 1까지 순서대로
    # answer에 추가
    else:
        for i in range(9, -1, -1):
            for _ in range(arr[i]):
                answer += str(i)
    # answer 출력
    return answer

print(solution())
