T= int(input())

for tc in range(1, T+1):
    row = int(input())
    farm = []
    for i in range(row):
        farm.append(list(map(str,input().split())))

    middle = int(row/2)
    start = 0
    end = row
    sum = 0

    for x in farm[middle:]:
        for y in x:
            for z in y[start:end]:
                sum = sum+int(z)
        start = start+1
        end = end-1

    start = 1
    end = row-1

    for p in reversed(farm[:middle]):
        for q in p:
            for r in q[start:end]:
                sum = sum+int(r)
        start = start+1
        end = end-1

    print(f"#{tc} {sum}")