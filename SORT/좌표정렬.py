import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())

posList = []

for _ in range(N):
    x,y = map(int,input().split())
    posList.append((x,y))

posList.sort()

for x, y in posList:
    print(x,y)