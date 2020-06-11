import sys
sys.stdin = open("input.txt","r")

N, M, K = map(int, input().split())


while N > 2 * M:
    N -= 1
    K -= 1

while N < 2 * M:
    M -= 1
    K -= 1

while K > 0:
    M -= 1
    N -= 2
    K -= 3

if M < 1 or N < 2:
    print(0)
else:
    print(M)
