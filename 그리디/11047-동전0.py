import sys
sys.stdin = open("input.txt","r")

N, K = map(int,input().split())
A = [int(input()) for _ in range(N)]

cnt = 0

for x in reversed(A):
    cnt += K//x
    K %= x

print(cnt)