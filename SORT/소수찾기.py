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


def setPrime():
    global numbers
    primes[0] = True
    primes[1] = True
    for i in range(2,1001):
        if primes[i] == False:
            if isPrime(i) == True:
                for j in range(i+i,1001,i):
                    primes[j] = True


numbers = [False] * 1001
N = int(input())

nums = list(map(int, input().split()))

setPrime()

cnt = 0
for x in nums:
    if not numbers[x]:
        cnt += 1

print(cnt)

