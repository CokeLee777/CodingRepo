#맵의 세로크기, 가로크기 입력
n,m = map(int, input().split())
#캐릭터의 시작위치와 바라보는 방향 입력
#방향 0:북,1:동,2:남,3:서
x,y,d = map(int, input().split())

#이동 반경 생성 -> 북,동,남,서 순서로 쓴다
dx = [-1,0,1,0]
dy = [0,-1,0,1]

nx = 0
ny = 0

visited = [[0]*m for _ in range(n)]

graph = []
#맵 생성 육지:0,바다:1 -> 캐릭터의 처음 위치는 항상 육지이다
for i in range(n):
    graph.append(list(map(int, input().split())))

#현재 위치 방문처리
graph[x][y] = 1
#방문한 칸의 갯수 세는 변수
count = 1
turncount = 0
while True:
    #왼쪽 방향으로 회전
    d -= 1
    #방향이 4가 될 경우 북쪽방향으로 처리
    if d == -1:
        d = 3
    #움직인 좌표 처리
    nx = x + dx[d]
    ny = y + dy[d]
    #현재 방향이 육지이고 가보지 않앗다면
    if graph[nx][ny] == 0 and visited[nx][ny] == 0:
        #현재 방향이 바다가 아니라면
        count += 1
        x = nx
        y = ny
        visited[nx][ny] = 1
        graph[nx][ny] = 1
    elif graph[x-dx[d]][y-dy[d]] != 1:
        x -= dx[d]
        y -= dy[d]
        continue
    else:
        break

print(count)