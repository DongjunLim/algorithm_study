

def solution(prices):
    answer = []
    length = len(prices)

    for i in range(length):
        end = True
        for j in range(i+1, length):
            if prices[i] > prices[j]:
                answer.append(j-i)
                end = False
                break
        if end:
            answer.append(length-1-i)

    return answer


def main():
    prices = [1, 2, 3, 2, 3]
    print(solution(prices))

if __name__ == '__main__':
    main()