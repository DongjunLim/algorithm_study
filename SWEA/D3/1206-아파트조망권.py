

for i in range(10):
    T = int(input())
    bList = list(map(int, input().split()))
    answer = 0

    for idx, x in enumerate(bList[2:-2],2):
        view = min(bList[idx]-bList[idx-1],bList[idx]-bList[idx-2],bList[idx]-bList[idx+1],bList[idx]-bList[idx+2])
        print(f"{idx}= {view}")
        if view > 0:
            answer = answer + view
    print(f"#{i+1} {answer}")

