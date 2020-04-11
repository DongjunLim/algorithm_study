n,m,k = 3,8,4

answer = 0





def foo(count,m,k):
    global answer
    if m == 0 and count == 0:
        answer = answer + 1
        return 0
    elif count == 0:
        return 0

    for i in range(1, k+1):
        foo(count-1,m-i,k)

    return 0


foo(n,m,k)
print(answer*2)