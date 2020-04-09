

n = int(input())
answer = ""
count = 0
for x in range(1, n+1):
    count = 0
    for y in str(x):
        if int(y) == 3 or int(y) == 6 or int(y) == 9:
            count = count + 1
    if count == 0:
        answer = answer + str(x)
    else:
        for z in range(count):
            answer = answer + "-"
    answer = answer + " "
print(answer[:-1])