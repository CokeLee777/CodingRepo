#p.262 전보
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

#노드(도시) 의 갯수, 간선(통로)의 갯수, 도착지 노드(메세지를 보내고자 하는 도시) 입력받기
n,m,c = map(int, input().split())

#시작 노드(메세지를 보내고자하는 도시)
start = c

#각 노드에 연결되어있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n+1)]

#간선에 대한 비용 무한으로 초기화
distance = [INF]*(n+1)

#x : 노드 번호, y : x와 이어진 노드, z : x,y와의 거리 입력받기
for _ in range(m):
    x,y,z = map(int, input().split())
    graph[x].append((y,z))

def dijkstra(start):
    #시작 위치 정보 초기화
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0
    #큐가 빌 때까지 반복
    while q:
        #가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist,now = heapq.heappop(q)
        #현재 노드에 대한 거리가 최단거리라면 패스
        if distance[now] < dist:
            continue
        
        #현재 노드와 연결된 다른 노드를 확인
        for i in graph[now]:
            cost = dist + i[1]
            #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

#다익스트라 알고리즘 수행
dijkstra(start)

#도달할 수 있는 노드의 갯수
count = 0
#도달 할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
max_distance = 0
for d in distance:
    #도달 할 수 있는 노드인 경우
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

#시작 노드는 제외해야 하므로 count - 1을 출력 
print(count - 1, max_distance)

