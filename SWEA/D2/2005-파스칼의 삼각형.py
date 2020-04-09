T= int(input())


for tc in range(1, T + 1):
    n = int(input())
    output = ''
    list = [[0 for j in range(n+2)] for i in range(n)]
    list[0][1] = 1
    for rowIdx, x in enumerate(list[1:],1):
        for colIdx, y in enumerate(x[1:-1],1):
            list[rowIdx][colIdx] = list[rowIdx-1][colIdx-1] + list[rowIdx-1][colIdx]

    print(f"#{tc}")
    for z in list:
        for a in z[1:-1]:
            if a != 0:
                output = output + str(a) + ' '
        print(output[:-1])
        output = ''