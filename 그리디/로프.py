import sys
sys.stdin = open("input.txt","r")

# 갯수 입력
N = int(input())

# 로프 중량 리스트 입력
rope = [int(input()) for _ in range(N)]

# 로프 중량순 으로 정렬
rope.sort()

maxW = 0

# 가장 작은 로프부터 하나씩 확인해본다.
for i in range(N):
    cnt = N - i
    maxW = max(rope[i]*cnt, maxW)

print(maxW)