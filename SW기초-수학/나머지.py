import sys
sys.stdin = open("input.txt","r")


A,B,C = map(int,input().split())

print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)