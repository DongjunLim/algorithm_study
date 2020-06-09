import sys
sys.stdin = open("input.txt","r")

T = int(input())
meetings = []
end = 0
cnt = 0
for i in range(T):
    meeting = tuple(map(int,input().split()))
    meetings.append(meeting)

meetings.sort()
meetings.sort(key= lambda element : element[1])

print(meetings)
for x in meetings:
    if x[0] < end:
        continue

    else:
        print(x)
        cnt += 1
        end = x[1]


print(cnt)