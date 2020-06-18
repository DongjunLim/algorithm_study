import sys

def dfs(num):
    if len(num) == 7:
        print(num)
        sys.exit()

    for i in range(1,4):
        if(isGood(num+str(i))):
            dfs(num+str(i))


def isGood(num):
    length = len(num)
    start = length - 1
    end = length
    print("num: ",num)
    for i in range(1,(length//2)+1):
        print(num[start-i:end-i], num[start:end])
        if num[start-i:end-i] == num[start:end]:
            return False
        start -= 1
    return True


sys.stdin = open("input.txt","r")
input = sys.stdin.readline

N = int(input())

dfs("1")