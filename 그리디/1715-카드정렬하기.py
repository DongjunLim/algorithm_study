import sys
sys.stdin = open("input.txt")


N = int(input())

cards = [int(input()) for _ in range(N)]

cards.sort()
print(cards)
length = len(cards)
for i in range(1,length):
    cards[i] = cards[i-1] + cards[i]

print(cards)
print(sum(cards[1:]))

