import heapq
import sys
sys.stdin = open("input.txt","r")


T = int(input())

for tc in range(1,T+1):
    V, E = map(int, input().split())
    answer = 0

    visited = [False] * (V+1)
    graph = [[] for _ in range(V+1)]
    queue = []

    ''' 입력데이터를 인접리스트로 저장. '''
    for i in range(E):
        v1,v2,w = map(int,input().split())
        graph[v1].append((w,v2))
        graph[v2].append((w,v1))

    ''' 시작 정점 0에 연결된 간선정보를 start 변수에 저장. '''
    start = graph[0]

    ''' 정점에 연결된 간선정보를 min heap으로 저장. '''
    for x in start:
        heapq.heappush(queue,x)

    ''' 시작 정점 방문 처리. '''
    visited[0] = True

    ''' 연결이 끊길때까지 반복. '''
    while queue != []:
        nowEdge = heapq.heappop(queue)
        nowWeight = nowEdge[0]
        nowVertex = nowEdge[1]

        if visited[nowVertex]:
            continue

        visited[nowVertex] = True
        answer += nowWeight

        next = graph[nowVertex]

        for x in next:
            heapq.heappush(queue,x)

    print(f'#{tc} {answer}')
