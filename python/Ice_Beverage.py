#p.149 음료수 얼려먹기

#얼음틀의 세로길이, 가로길이 입력
row, column = map(int, input().split())

#얼음틀 생성
graph = []
for i in range(row):
    graph.append(list(map(int, input())))

#DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    #얼음틀을 벗어나는 경우 즉시 종료
    if x <= -1 or x >= row or y <= -1 or y >= column:
        return False

    #현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        #해당 노드 방문처리
        graph[x][y] = 1
        #상,하,좌,우 재귀호출
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

#모든 노드(위치) 에 대하여 음료수 채우기
result = 0
for i in range(row):
    for j in range(column):
        #현재 위치에서 DFS 수행
        if dfs(i,j) == True:
            result += 1

print(result)
