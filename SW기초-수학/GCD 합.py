import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

T = int(input())

for tc in range(1,T+1):
    numbers = list(map(int,input().split()))
    length = len(numbers)
    total = 0

    for i in range(1,length):
        for j in range(i+1,length):
            total += gcd(numbers[i],numbers[j])
    sys.stdout.write(f'{total}\n')