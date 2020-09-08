#p.118 게임개발

#세로크기 N 가로크기 M 을 입력
N,M = map(int, input().split())
#캐릭터의 시작위치, 방향을 입력
stX,stY,Dir = map(int, input().split())

#맵 생성
Map = []
for i in range(0,N):
    Map.append(list(map(int, input().split())))

#캐릭터의 처음위치를 방문했다고 저장 
Map[stX][stY] = 1
num = 1

while True:
    if Dir == 0:    #캐릭터 방향이 북쪽일때
        Dir += 1
        if stX - 1 >= 0 and stX - 1 <= M - 1:
            if Map[stX-1][stY] == 0:
                Map[stX-1][stY] = 1
                stX -= 1
                num += 1
            elif Map[stX+1][stY] == 1 and Map[stX-1][stY] == 1 and Map[stX][stY+1] == 1 and Map[stX][stY-1] == 1:
                break
    elif Dir == 1:  #캐릭터 방향이 동쪽일때
        Dir += 1
        if stY - 1 >= 0 and stY - 1 <= N - 1:
            if Map[stX][stY-1] == 0:
                Map[stX][stY-1] = 1
                stY -= 1
                num += 1
            elif Map[stX+1][stY] == 1 and Map[stX-1][stY] == 1 and Map[stX][stY+1] == 1 and Map[stX][stY-1] == 1:
                break
    elif Dir == 2:  #캐릭터 방향이 남쪽일때
        Dir += 1
        if stX + 1 >= 0 and stX + 1 <= M - 1:
            if Map[stX+1][stY] == 0:
                Map[stX+1][stY] = 1
                stX += 1
                num += 1
            elif Map[stX+1][stY] == 1 and Map[stX-1][stY] == 1 and Map[stX][stY+1] == 1 and Map[stX][stY-1] == 1:
                break
    elif Dir == 3:  #캐릭터 방향이 서쪽일때
        Dir -= 3
        if stY + 1 >= 0 and stY + 1 <= N - 1:
            if Map[stX][stY+1] == 0:
                Map[stX][stY+1] = 1
                stY += 1
                num += 1
            elif Map[stX+1][stY] == 1 and Map[stX-1][stY] == 1 and Map[stX][stY+1] == 1 and Map[stX][stY-1] == 1:
                break

print(num)

