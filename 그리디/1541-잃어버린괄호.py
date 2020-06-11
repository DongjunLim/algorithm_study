import sys
sys.stdin = open("input.txt","r")

op = ['+','-']

expression = input()
print(expression)
sp = expression.split('-')
answer = []
for x in sp:
    temp = x.split('+')
    intTemp = [int(x) for x in temp]
    tempSum = sum(intTemp)
    if answer == []:
        answer.append(tempSum)
    else:
        answer.append(0-tempSum)

print(sum(answer))


