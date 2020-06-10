import sys
sys.stdin = open("input.txt","r")

coin = [500,100,50,10,5,1]

money = 1000 - int(input())
cnt = 0

for x in coin:
    if x > money:
        continue
    cnt += money // x
    money %= x

print(cnt)
