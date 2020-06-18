import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
write = sys.stdout.write
MAX = 1000001
numbers = []
primes = []
n = []
def isPrime(num):
    if num == 2 or num == 3:
        return True

    for i in range(2,int(num**(0.5))+1):
        if num % i == 0:
            return False
    return True

def setPrimes():
    global numbers, MAX, primes
    numbers[0] = False
    numbers[1] = False
    for i in range(2,MAX):
        if numbers[i] and isPrime(i):
            primes.append(i)
            for j in range(i*2,MAX,i):
                numbers[j] = False

while True:
    ipt = int(input())
    if ipt == 0:
        break
    n.append(ipt)

MAX = max(n)
numbers = [True] * (MAX+1)
setPrimes()

for q in n:
    a = False
    for i, x in enumerate(primes):
        if q < x:
            break
        if numbers[q-x]:
            a = x
            b = q-x
            break

    if not a:
        write("Goldbach's conjecture is wrong.\n")
    else:
        write(f'{q} = {a} + {b}\n')