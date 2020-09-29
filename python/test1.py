#맵의 세로크기 가로크기 입력받기
n,m = map(int, input().split())

#방문한 위치를 저장하기 위한 맵 생성
visited = [[0]*m for _ in range(n)]

#게임 캐릭터의 시작좌표와 바라보는 방향 입력
x,y,direction = map(int, input().split())
#시작 위치 방문처리
visited[x][y] = 1

#맵 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

#북 서 남 동 순으로 리스트 생성
dx = [-1,0,1,0]
dy = [0,-1,0,1]

#반시계방향으로 회전하는 함수 생성
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_count = 0
#게임 시작
while True:
    #반시계 방향 회전
    turn_left()
    turn_count += 1
    nx = x + dx[direction]
    ny = y + dy[direction]
    #캐릭터가 가보지않은 칸이거나 바다가 아닌경우
    if visited[nx][ny] == 0 and graph[nx][ny] != 1:
        x = nx
        y = ny
        visited[nx][ny] = 1
        count += 1
        turn_count = 0
    elif visited[nx][ny] != 0 and turn_count != 4:
        continue
    
    #캐릭터가 네 방향모두 이미 가본칸이거나 바다로 되어있는경우
    if turn_count == 4 and graph[x-dx[direction]][y-dy[direction]] != 1:
        x -= dx[direction]
        y -= dy[direction]
        continue 
    
    if turn_count == 4 and graph[x-dx[direction]][y-dy[direction]] == 1:
        break

    

print(count)