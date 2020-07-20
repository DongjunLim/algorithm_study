def solution(budgets, M):
    left = 1
    right = max(budgets)

    while left <= right:
        mid = (left + right) // 2
        budgetSum = 0
        for budget in budgets:
            if budget > mid:
                budgetSum += mid
            else:
                budgetSum += budget
        if budgetSum > M:
            right = mid - 1
        else:
            left = mid + 1
            answer = mid

    return answer


def main():
    budgets = [120, 110, 140, 150]
    M = 485
    print(solution(budgets, M))


if __name__ == '__main__':
    main()