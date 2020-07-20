def solution(n, times):
    answer = 1000000000
    left = 1
    right = 1000000000 ** 2

    while left <= right:
        mid = (left + right) // 2
        s = 0
        for worker in times:
            s += (mid // worker)

        if n <= s:
            right = mid - 1
            answer = min(answer, mid)
        else:
            left = mid + 1

    return answer


n = 6
time = [7, 10]

print(solution(n, time))