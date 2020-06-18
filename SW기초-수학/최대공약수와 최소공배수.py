import sys
sys.stdin = open("input.txt","r")
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

T = int(input())


for tc in range(1,T+1):
    A, B = map(int, input().split())
    print((A*B)//gcd(A,B))








