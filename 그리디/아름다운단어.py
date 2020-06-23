import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())
word = list(input())
if word[-1] == '\n':
    del word[-1]

length = len(word)

alphabet = {}


aList = []

for i, x in enumerate(word):
    if not x in alphabet:
        aList.append(x)
        alphabet[x] = []
    alphabet[x].append(i)

isSangkeunsTurn = True

answer = []
sangkeun = []

aList.sort()
i = length-1
sIdx = i

while i > -1:
    if isSangkeunsTurn:
        if word[sIdx] == -1:
            sIdx -= 1
            continue
        choice = word[sIdx]
        alphabet[choice].pop()

        sangkeun.append(choice)
        isSangkeunsTurn = False
        sIdx -= 1

    else:
        for target in aList:
            if not target in alphabet:
                continue

            temp = alphabet[target]

            if temp != []:
                idx = temp.pop()
                choice = word[idx]
                answer.append(choice)
                word[idx] = -1
                break
        isSangkeunsTurn = True

    i -= 1



sangkeun = ''.join(sangkeun)
answer = ''.join(answer)



if answer < sangkeun:
    print("DA")
    print(answer)
else:
    print("NE")
    print(answer)
