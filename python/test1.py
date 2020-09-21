import heapq

q = []

heapq.heappush(q, (1,2))
heapq.heappush(q, (0,1))
print(heapq.heappop(q))
print(heapq.heappop(q))