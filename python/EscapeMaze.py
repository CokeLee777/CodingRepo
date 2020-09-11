#p.152 미로탈출

#deque 라이브러리 호출
from collections import deque
#미로의 행,열의 갯수
row, column = map(int, input().split()) 

#맵 그리기
graph = []
for i in range(row):
    graph.append(list(map(int, input().split())))
    
#bfs 함수 만들기
def bfs(graph, start, visited):
    #deque 라이브러리 사용
    queue = deque([[]*row])
    

    

