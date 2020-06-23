import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline


N = int(input())

lst = list(map(int, input().split()))

answer = set(lst)

print(len(answer))