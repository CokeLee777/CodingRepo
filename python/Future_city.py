#p.259 미래도시

#무한을 표기하기 위한 변수 선언
INF = int(1e9)
#노드(회사) 의 갯수와 간선(경로)의 갯수 입력받기
n,m = map(int, input().split())

#노드들이 연결된 그래프 무한으로 초기화하기
graph = [[INF]*(n+1) for _ in range(n+1)]

#자기 자신으로 가는 비용 0으로 초기화
for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0

#연결된 노드들 입력
for _ in range(m):
    a,b= map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

#도착지와 경유지 입력
X,K = map(int, input().split())

#플로이드 알고리즘 수행
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

#최소 이동 시간 구하기
if graph[1][K] + graph[K][X] >= INF:
    print('infinity')
else:
    print(graph[1][K] + graph[K][X])
