T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    answer = round(sum(arr)/len(arr))
    print(f"#{tc} {answer}")

