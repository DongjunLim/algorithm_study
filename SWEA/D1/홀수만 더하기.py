T = int(input())

for tc in range(T) :
    nums = list(map(int, input().split()))
    print(nums)
    res = sum(n for n in nums if n%2==1)
    print( f"#{tc+1} {res}" )
