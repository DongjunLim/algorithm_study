T = int(input())
cache = [[False for j in range(20)] for i in range(20)]

for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    print(A)

def find(lst,x,y):












from itertools import combinations

T = int(input())

for tc in range(1,T+1):
    N, K = map(int, input().split())
    A = list(map(str, input().split()))
    sum = 0
    count = 0
    for i in range(1, len(A)):
        temp = list(map(''.join, combinations(A, i)))
        for j in temp:
            for k in j:
                sum = sum+int(k)
            if sum == K:
                count = count + 1
            sum = 0

    print(f"#{tc} {count}")
