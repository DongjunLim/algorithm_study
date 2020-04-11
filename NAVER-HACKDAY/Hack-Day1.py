def solution(n, delivery):
    answer = ''
    stockList = ["?" for i in range(n + 1)]
    for x in delivery:
        if x[2] == 1:
            stockList[x[0]] = "O"
            stockList[x[1]] = "O"
            for y in delivery:
                if (y[0] == x[0] or y[0] == x[1]) and y[2] == 0:
                    stockList[y[1]] = "X"
                elif (y[1] == x[0] or y[1] == x[1]) and y[2] == 0:
                    stockList[y[0]] = "X"
        else:
            if stockList[x[0]] == "O":
                stockList[x[1]] = "X"
            elif stockList[x[1]] == "O":
                stockList[x[0]] = "X"

    for i in stockList[1:]:
        answer = answer + i
    return answer