#무한을 의미하는 값으로 10억을 설정
INF = int(1e9)

#노드의 갯수 및 간선의 갯수 입력받기
n,m = map(int, input().split())

#2차원 리스트 그래프 표현, 모든 값을 무한으로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]

print(graph)
