from itertools import permutations

INF = 9999999


def set_prime(n):
    global prime, INF
    prime = [True] * (INF+1)
    prime[0] = False
    prime[1] = False

    m = int(INF ** 0.5)

    for i in range(2, m+1):
        if prime[i]:
            for j in range(i+i, INF+1, i):
                prime[j] = False

    return


def solution(numbers):
    global prime, INF
    answer = set()
    set_prime(int(numbers))
    permute = []
    for i in range(1, len(numbers)+1):
        permute += permutations(numbers,i)

    for x in permute:
        nxt = int(''.join(x))
        if prime[nxt]:
            answer.add(nxt)

    return len(answer)


print(solution("17"))