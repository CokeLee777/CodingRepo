#p.152 미로탈출

#deque 라이브러리 호출
from collections import deque
#미로의 행,열의 갯수
row, column = map(int, input().split()) 

#맵 그리기
graph = []
for i in range(row):
    graph.append(list(map(int, input())))

print(graph)
#이동반경 정하기    
dx = [-1,1,0,0]
dy = [0,0,-1,1]

#bfs 함수 만들기
def bfs(x, y):
    #deque 라이브러리 사용
    queue = deque([])
    queue.append((x,y))

    #큐가 빌 때까지 반복
    while queue:
        #먼저 들어간 것이 먼저 나온다. -> 큐 연산
        x, y = queue.popleft()
        #현재 위치에서 네 방향으로의 위치확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= row or 
            
            ny >= column:
                continue
            #괴물이 있는 경우 무시
            if graph[nx][ny] == 0:
                continue
            #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    #가장 오른쪽 아래까지의 최단거리 반환
    return graph[row-1][column-1]

print(bfs(0,0))


    

