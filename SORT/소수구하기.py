import sys
import math
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

def isPrime(num):
    if num == 2 or num == 3:
        return True
    for i in range(2,int(math.sqrt(num))):
        if num % i == 0:
            return False
    return True


def setPrime(n):
    global numbers
    primes[0] = True
    primes[1] = True
    for i in range(2,n+1):
        if primes[i] == False:
            if isPrime(i) == True:
                for j in range(i+i,n+1,i):
                    primes[j] = True


numbers = [False] * 1000001

M,N = map(int, input().split())

setPrime(N)

for i in range(M,N+1):
    if not numbers[i]:
        sys.stdout.write(f'{i}\n')


