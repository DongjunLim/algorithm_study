import sys

def plus(num,type):
    if type == 'E':
        limit = eLimit
    elif type == 'S':
        limit = sLimit
    elif type == 'M':
        limit = mLimit

    num = (num +1) % limit
    if num == 0:
        num += 1
    return num

sys.stdin = open("input.txt", "r")

E, S, M = map(int,input().split())
eLimit, sLimit, mLimit = 16, 29, 20


cnt = 0
e, s, m = 1,1,1

while True:
    cnt += 1
    if e == E and s == S and m == M:
        print(cnt)
        break

    e = plus(e,'E')
    s = plus(s,'S')
    m = plus(m,'M')


