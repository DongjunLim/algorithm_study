import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

N = int(input())

numbers = [int(input()) for _ in range(N)]

numbers.sort()
answer = []
length = len(numbers)
i=length-1

while i > 0:
    if numbers[i-1] < 2:
        break
    numbers[i-1] *= numbers[i]
    del numbers[i]

    i -= 2


i = 0
length = len(numbers)
while i < length-1:

    if numbers[i+1] > -1:
        if numbers[i+1] == 0:
            numbers[i] *= numbers[i+1]
        break

    numbers[i] *= numbers[i+1]
    numbers[i+1] = 0
    i += 2

print(sum(numbers))
