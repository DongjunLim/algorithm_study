import sys
sys.stdin = open("input.txt","r")
num = 7
MAX = 9
candidates = []

def dfs(idx):
    global candidates,length,height
    if idx == num:
        if sum(candidates) == 100:
            for x in candidates:
                print(x)
            sys.exit()
        return

    for i in range(idx,MAX):
        candidates.append(height[i])
        dfs(idx+1)
        candidates.pop()

height = [int(input()) for _ in range(MAX)]

height.sort()

dfs(0)